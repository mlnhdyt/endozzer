from rest_framework import serializers
from .models import Campaign, JoinCampaign

class CampaignSerializer(serializers.ModelSerializer):
	author = serializers.CharField(read_only=True)
	created_at = serializers.DateTimeField(read_only=True)

	class Meta:
		model = Campaign
		fields = ['pk', 'author', 'judul', 'deskripsi', 'created_at', 'lunas', 'fee']
		extra_kwargs = {
			'pk': {'read_only': True},
			'judul': {'required': True},
			'deskripsi': {'required': True},
			'fee': {'required': True}
		}

	def __init__(self, *args, **kwargs):
		super(CampaignSerializer, self).__init__(*args, **kwargs)
		if(self.context['request'].user.is_company == False):
			self.fields.pop('lunas')
		
class JoinCampaignSerializer(serializers.ModelSerializer):
	campaign_id = serializers.IntegerField()
	author = serializers.CharField(read_only=True)
	created_at = serializers.DateTimeField(read_only=True)

	class Meta:
		model = JoinCampaign
		fields = ['pk', 'campaign_id', 'author', 'status', 'created_at']
		extra_kwargs = {
			'campaign_id': {'required': True}
		}


	def validate(self, attrs):
		try:
			attrs["campaign_id"] = Campaign.objects.get(pk=attrs["campaign_id"])
		except:
			raise serializers.ValidationError({"campaign_id": "campaign_id fields didn't match."})

		joinCampaign = JoinCampaign.objects.filter(campaign_id=attrs["campaign_id"], author=self.context['request'].user)

		if(joinCampaign.exists()):
			raise serializers.ValidationError({"campaign_id": "kamu sudah mendaftar campaign ini."})

		return attrs

	def create(self, data):
		# print(type(data["campaign"]))
		joinCampaign = JoinCampaign.objects.create(
				campaign = data["campaign_id"],
				author = self.context['request'].user
			)
		joinCampaign.save()
		return joinCampaign

