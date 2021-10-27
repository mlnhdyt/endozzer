from django.urls import include, path
from auth.views import RegisterView
from rest_framework_simplejwt.views import (
		TokenObtainPairView,
		TokenRefreshView,
	)

urlpatterns = [
	path('token/', TokenObtainPairView.as_view(), name='Token Obtain Pair'),
	path('token/refresh', TokenRefreshView.as_view(), name='Token refresh'),
	path('register/', RegisterView.as_view(), name='Register'),
]