from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import PaymentSerializer

from campaigns.permissions import IsPostAndCompany 
# Create your views here.

class PaymentCreateView(CreateAPIView):

	serializer_class = PaymentSerializer
	permission_classes = (IsAuthenticated, IsPostAndCompany,)

# class TransactionCreateView(CreateAPIView):
# 	serializer_class = PaymentTxSerializer

	