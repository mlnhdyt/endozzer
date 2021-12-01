from django.urls import path
from .views import *

urlpatterns = [
	path('influenzer/', InfluenzerListCreateView.as_view(), name='Influenzer List Create'),
	path('influenzer/<pk>/', InfluenzerRetrieveView.as_view(), name='Influenzer Detail'),
	path('company/', CompanyCreateView.as_view(), name='Company Create'),
	path('company/<pk>/', CompanyRetrieveView.as_view(), name='Company Detail'),
]