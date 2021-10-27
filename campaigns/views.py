from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import CampaignSerializer, JoinCampaignSerializer
from .models import Campaign, JoinCampaign
from .permissions import IsOwner, IsPostAndCompany, IsPatchDeleteAndOwner, IsCompanyAndOwner, IsGetAndInfluenzer, IsPostAndInfluenzer

class CampaignListCreateView(ListCreateAPIView):
	serializer_class = CampaignSerializer
	permission_classes = (IsAuthenticated, IsPostAndCompany)
	queryset = Campaign.objects.all()

	def get_queryset(self):
		qs = super().get_queryset()
		user = self.request.user

		if(user.is_company == True):
			return qs.filter(author=user)

		return qs

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)


class CampaignDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Campaign.objects.all()
	serializer_class = CampaignSerializer
	permission_classes = (IsAuthenticated, IsPatchDeleteAndOwner, IsCompanyAndOwner, IsGetAndInfluenzer)


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
	# def perform_create(self, serializer):
		# serializer.save(influenzer=self.request.user, campaign=)