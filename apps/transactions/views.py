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

        # Get the token using the PeoplesPayService from the .get_token() method
        token = PeoplesPayService.get_token()
        print(token)
        if token is None:
            return Response(
                {"message": "Failed to retrieve token"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if payment_serializer.is_valid():
            validated_data = payment_serializer.validated_data
        # Disburse payment
        disburse_payload = {
            "amount": str(validated_data["amount"]),
            "account_number": validated_data["account_number"],
            "account_name": validated_data["account_name"],
            "account_issuer": validated_data["account_issuer"],
            # "external_transaction_id": validated_data["external_transaction_id"],
            "description": "Payment description",
        }
        disburse_headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token['data']}",
        }

        try:
            disburse_response = requests.post(
                f"{PeoplesPayService.BASE_URL}/disburse",
                json=disburse_payload,
                headers=disburse_headers,
            )
            print(disburse_headers)
            disburse_data = disburse_response.json()

            print(disburse_data)

            if disburse_response.status_code == 200 and disburse_data.get("success"):
                payment_serializer.save()  # Save payment record to the database
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


class CollectionsView(APIView):
    def post(self, request):
        collection_serializer = CollectionsSerializer(data=request.data)

        if collection_serializer.is_valid():
            validated_data = collection_serializer.validated_data

            # Get the token using the PeoplesPayService
            token = PeoplesPayService.get_token()
            print(f"second token: {token}")
            if token is None:
                return Response(
                    {"message": "Failed to retrieve token"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Process the collection
            collection_payload = {
                "amount": str(validated_data["amount"]),
                "account_number": validated_data["account_number"],
                "account_name": validated_data["account_name"],
                "account_issuer": validated_data["account_issuer"],
                "callbackUrl": validated_data["callback_url"],
                "description": "Collection description",
            }
            collection_headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {token['data']}",
            }

            try:
                collection_response = requests.post(
                    f"{PeoplesPayService.BASE_URL}/collectmoney",
                    json=collection_payload,
                    headers=collection_headers,
                )
                collection_data = collection_response.json()

                if collection_response.status_code == 200 and collection_data.get(
                    "success"
                ):
                    collection_serializer.save()  # Save collection record to the database
                    return Response(
                        {"message": "Collection processed successfully"},
                        status=status.HTTP_201_CREATED,
                    )
                else:
                    return Response(
                        {
                            "message": collection_data.get(
                                "message", "Collection failed"
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            except requests.exceptions.RequestException as e:
                return Response(
                    {"message": f"Error processing collection: {str(e)}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            collection_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class PaymentCallbackAPIView(APIView):
    def post(self, request):
        transaction_id = request.data.get("transactionId")
        status = request.data.get("success")

        # Find the collection related to this transaction using external_transaction_id
        try:
            collection = Collections.objects.get(external_transaction_id=transaction_id)
            if status == "true":
                collection.transaction_status = "completed"
            else:
                collection.transaction_status = "failed"
            collection.save()

            return Response(
                {"message": "Callback processed successfully"},
                status=status.HTTP_200_OK,
            )
        except Collections.DoesNotExist:
            return Response(
                {"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND
            )
