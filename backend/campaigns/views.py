from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView



from .serializers import *
from .models import *
from .permissions import IsOwner, IsPostAndCompany, IsPatchDeleteAndOwner, IsCompanyAndOwner, IsGetAndInfluenzer, IsPostAndInfluenzer, IsInfluencerAndOwner
from .utils import get_tx_status

from payment.models import Payment
from payment.utils import tx_status

from accounts.models import Influenzer


from django.utils import timezone

class CampaignListCreateView(ListCreateAPIView):
	serializer_class = CampaignSerializer
	permission_classes = (IsAuthenticated, IsPostAndCompany)
	queryset = Campaign.objects.all()

	def get_queryset(self):
		qs = super().get_queryset()
		user = self.request.user

		if(user.is_company == True):
			return qs.filter(author=user)
		else:
			return qs.filter(periode_start__lte=timezone.now())

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class CampaignDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Campaign.objects.all()
	serializer_class = CampaignSerializer
	permission_classes = (IsAuthenticated, IsPatchDeleteAndOwner, IsCompanyAndOwner,)

	def get_queryset(self):
		qs = super().get_queryset()
		user = self.request.user

		if(user.is_company == False):
			return qs.filter(periode_start__lte=timezone.now())
		else:
			return qs


class JoinCampaignListCreateView(ListCreateAPIView):
	serializer_class = JoinCampaignSerializer
	queryset = JoinCampaign.objects.all()
	permission_classes = (IsAuthenticated, IsPostAndInfluenzer)

	def get_queryset(self):
		qs = super().get_queryset()
		user = self.request.user

		if(user.is_company == False):
			return qs.filter(author=user)
		else:
			return qs.filter(campaign__author=user)
		return qs

	# def create(self, request, *args, **kwargs):
 #    	# ''' I wanted to do some stuff with serializer.data here '''
	# 	instance = self.get_object()
	# 	print(instance)
	# 	return super(MemberCreate, self).create(request, *args, **kwargs)

	# def list(self, request, *args, **kwargs):
	# 	queryset = self.filter_queryset(self.get_queryset())

	# 	page = self.paginate_queryset(queryset)
	# 	if page is not None:
	# 		serializer = self.get_serializer(page, many=True)
	# 		print(serializer.data, end='aaaa')

	# 		return self.get_paginated_response(serializer.data)
	
	# 	serializer = self.get_serializer(queryset, many=True)
	# 	print(serializer.data, end='bbbb')
	# 	return Response(serializer.data)

	# def perform_create(self, serializer):
		# serializer.save(influenzer=self.request.user, campaign=)

class JoinCampaignDetailView(RetrieveUpdateDestroyAPIView):
	queryset = JoinCampaign.objects.all()
	serializer_class = JoinCampaignSerializer
	permission_classes = (IsAuthenticated, IsInfluencerAndOwner, IsCompanyAndOwner)


class ImgCreateView(UpdateAPIView):
	queryset = Campaign.objects.all()
	parser_classes = [MultiPartParser, FormParser]
	permission_classes = (IsAuthenticated,IsCompanyAndOwner)
	serializer_class = ImgCreateSerializer


class ExampleCreateView(UpdateAPIView):
	queryset = Campaign.objects.all()
	parser_classes = [MultiPartParser, FormParser]
	permission_classes = (IsAuthenticated,IsCompanyAndOwner)
	serializer_class = ExampleCreateSerializer


class DraftPostCreateView(UpdateAPIView):
	queryset = JoinCampaign.objects.all()
	parser_classes = [MultiPartParser, FormParser]
	permission_classes = (IsAuthenticated,IsInfluencerAndOwner)
	serializer_class = DraftPostSerializer

	def perform_update(self, serializer):
		serializer.save(draft_status=2)

class PostCreateView(UpdateAPIView):
	queryset = JoinCampaign.objects.all()
	parser_classes = [MultiPartParser, FormParser]
	permission_classes = (IsAuthenticated,IsInfluencerAndOwner)
	serializer_class = PostSerializer

	def perform_update(self, serializer):
		serializer.save(status=4)
		instance = self.get_object()
		inf = Influenzer.objects.get(user=instance.author)
		inf.balance += instance.campaign.fee
		inf.save()


