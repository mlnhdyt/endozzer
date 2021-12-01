from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class InfluenzerListCreateView(ListCreateAPIView):
	queryset = Influenzer.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = InfluenzerSerializer

class InfluenzerRetrieveView(RetrieveUpdateAPIView):
	queryset = Influenzer.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = InfluenzerSerializer


class CompanyCreateView(CreateAPIView):
	queryset = Company.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = CompanySerializer

class CompanyRetrieveView(RetrieveUpdateAPIView):
	queryset = Company.objects.all()
	permission_classes = (IsAuthenticated, )
	serializer_class = CompanySerializer