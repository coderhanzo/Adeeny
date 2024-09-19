from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Payments, Collections
from .serializers import PaymentsSerializer, CollectionsSerializer
from .services import PeoplesPayService


class PaymentsView(APIView):
    def post(self, request):
        payment_serializer = PaymentsSerializer(data=request.data)
        if payment_serializer.is_valid():
            # Extract validated data from the serializer
            validated_data = payment_serializer.validated_data
            token_response = PeoplesPayService.get_token(
                merchant_id="your_merchant_id", api_key="your_api_key"
            )
            token = token_response.get("data")

            if not token:
                return Response(
                    {"message": "Failed to retrieve token"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Use PeoplesPayService to disburse the money
            response = PeoplesPayService.disburse_money(
                token=token,
                amount=validated_data["amount"],
                account_name=validated_data["account_name"],
                account_number=validated_data["account_number"],
                account_issuer=validated_data["account_issuer"],
                external_transaction_id=validated_data["external_transaction_id"],
            )

            if response["success"]:
                payment_serializer.save()  # Save payment record in the database
                return Response(
                    {"message": "Payment processed successfully"},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"message": response["message"]}, status=status.HTTP_400_BAD_REQUEST
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
