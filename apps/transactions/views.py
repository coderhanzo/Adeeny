from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payments, Collections
from .serializers import PaymentsSerializer, CollectionsSerializer
from .services import PeoplesPayService
import requests

class PaymentsView(APIView):
    def post(self, request):
        payment_serializer = PaymentsSerializer(data=request.data)

        if payment_serializer.is_valid():
            validated_data = payment_serializer.validated_data

            # we generate the token here
            url = "https://peoplespay.com.gh/peoplepay/hub/token/get"
            payload = {
                "merchant_id": "66e058b1a69d30672127d1b6",
                "api_key": "6dfbecfd-d091-40ff-9ed1-2e8324d12a35",
            }
            headers = {"Content-Type": "application/json"}

            try:
                token_response = requests.post(
                    url, json=payload, headers=headers, timeout=10
                )
                token_data = token_response.json()

                if token_response.status_code == 200 and "data" in token_data:
                    token = token_data["data"]
                else:
                    return Response(
                        {"message": "Failed to retrieve token"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            except requests.exceptions.RequestException as e:
                return Response(
                    {"message": f"Error retrieving token: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            disburse_url = "https://peoplespay.com.gh/peoplepay/hub/disburse"
            disburse_payload = {
                "amount": str(validated_data["amount"]),
                "account_number": validated_data["account_number"],
                "account_name": validated_data["account_name"],
                "account_issuer": validated_data["account_issuer"],
                "external_transaction_id": validated_data["external_transaction_id"],
            }
            disburse_headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token}",
            }

            try:
                disburse_response = requests.post(
                    disburse_url, json=disburse_payload, headers=disburse_headers
                )
                disburse_data = disburse_response.json()

                # Check if disbursement was successful
                if disburse_response.status_code == 200 and disburse_data.get(
                    "success"
                ):
                    payment_serializer.save()  # Save the payment record to the database
                    return Response(
                        {"message": "Payment processed successfully"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {"message": disburse_data.get("message", "Payment failed")},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            except requests.exceptions.RequestException as e:
                return Response(
                    {"message": f"Error processing payment: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionsView(APIView):
    def post(self, request):
        collection_serializer = CollectionsSerializer(data=request.data)
        if collection_serializer.is_valid():
            # Use PeoplesPayService to process the collection
            response = PeoplesPayService.process_collection(
                collection_serializer.validated_data
            )
            if response["success"]:
                collection_serializer.save()  # Save collection record in database
                return Response(
                    {"message": "Collection processed successfully"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"message": response["message"]}, status=status.HTTP_400_BAD_REQUEST
                )
        return Response(
            collection_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PaymentCallbackAPIView(APIView):
    def post(self, request):
        transaction_id = request.data.get("transactionId")
        status = request.data.get("success")

        # Find the collection related to this transaction
        try:
            collection = Collections.objects.get(external_transaction_id=transaction_id)
            if status == "true":
                collection.transaction_status = "completed"
            else:
                collection.transaction_status = "failed"
            collection.save()
            return Response(
                {"message": "Callback processed"}, status=status.HTTP_200_OK
            )
        except Collections.DoesNotExist:
            return Response(
                {"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND
            )
