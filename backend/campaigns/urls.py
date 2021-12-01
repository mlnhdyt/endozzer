from django.urls import path
from .views import *

urlpatterns = [
	path('', CampaignListCreateView.as_view(), name='Campaign List Create'),
	path('detail/<pk>/', CampaignDetailView.as_view(), name='Campaign Detail'),
	path('join/', JoinCampaignListCreateView.as_view(), name='JoinCampaign List Create'),
	path('join/detail/<pk>/', JoinCampaignDetailView.as_view(), name='JoinCampaign Detail'),
	path('draft/<pk>/', DraftPostCreateView.as_view(), name='Draft Post Create'),
	path('post/<pk>/', PostCreateView.as_view(), name='Post Create'),
	path('img/<pk>/', ImgCreateView.as_view(), name='Img Create'),
	path('example/<pk>/', ExampleCreateView.as_view(), name='Example Create'),
]