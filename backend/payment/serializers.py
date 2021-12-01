from rest_framework import serializers
from .models import Payment

from .utils import generate_tx
from campaigns.utils import get_tx_status

from campaigns.models import JoinCampaign

class PaymentSerializer(serializers.ModelSerializer):
	joinCampaign_id = serializers.IntegerField(write_only=True, required=True)
	created_at = serializers.DateTimeField(read_only=True)
	token = serializers.CharField(read_only=True, max_length=40)
	status = serializers.CharField(read_only=True)

	class Meta:
		model = Payment
		fields = ['joinCampaign_id', 'token', 'order_id', 'status', 'created_at']
	
	def validate(self, attrs):
		try:
			joinCampaign = JoinCampaign.objects.get(pk=attrs["joinCampaign_id"])
		except:
			raise serializers.ValidationError({"error": "joinCampaign_id tidak valid"})

		if(get_tx_status(joinCampaign)):
			raise serializers.ValidationError({"error": "sudah dibayar"})

		return attrs

	def create(self, data):
		joinCampaign = JoinCampaign.objects.get(pk=data["joinCampaign_id"])
		order_id, token = generate_tx(self.context["request"].user, joinCampaign.campaign.fee)
		payment = Payment.objects.create(
			joinCampaign=joinCampaign,
			order_id=order_id,
			token=token
		)
		payment.save()
		return payment


# class PaymentTxSerializer(serializers.ModelSerializer):
# 	order_id = serializers.CharField(write_only=True, required=True)
# 	transaction_status = serializers.CharField(write_only=True, required=True)

# 	class Meta:
# 		model = PaymentTx
# 		fields = ('transaction_id', 'transaction_status', 'order_id')
# 		extra_kwargs = {
# 			'transaction_id': {'required': True, 'validators': []}
# 		}

# 	def create(self, data):

# 		tx = PaymentTx.objects.filter(transaction_id=data['transaction_id'])
# 		update = False

# 		if tx.exists():
# 			update = True

# 		lunas = False
# 		if(data['transaction_status'] == 'capture' or data['transaction_status'] == 'settlement'):
# 			lunas = True

# 		if update:
# 			tx = tx.get()

# 			if(str(tx.payment.order_id) != data['order_id']):
# 				raise serializers.ValidationError({'order_id': 'tidak sama'})

# 			tx.lunas=lunas
# 			tx.save()

# 		else:
# 			tx = PaymentTx.objects.create(
# 					transaction_id=data['transaction_id'],
# 					payment=Payment.objects.get(order_id=data['order_id']),
# 					lunas=lunas
# 				)
# 			tx.save()

# 		return tx