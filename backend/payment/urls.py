from django.urls import path
from .views import PaymentCreateView

urlpatterns = [
	path('generate', PaymentCreateView.as_view(), name='Payment Create'),
	# path('', TransactionCreateView.as_view(), name='Transaction Create'),

]