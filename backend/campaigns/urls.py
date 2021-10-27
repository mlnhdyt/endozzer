from django.urls import path
from .views import CampaignListCreateView, CampaignDetailView, JoinCampaignListCreateView

urlpatterns = [
	path('', CampaignListCreateView.as_view(), name='Campaign List Create'),
	path('detail/<pk>/', CampaignDetailView.as_view(), name='Campaign Detail'),
	path('join/', JoinCampaignListCreateView.as_view(), name='JoinCampaign List Create'),

]