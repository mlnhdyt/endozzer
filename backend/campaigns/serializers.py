from rest_framework import serializers
from .models import Campaign, JoinCampaign
from .utils import get_tx_status

from django.utils import timezone


class CampaignSerializer(serializers.ModelSerializer):
	author = serializers.CharField(read_only=True)
	created_at = serializers.DateTimeField(read_only=True)



	# gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE, default=0)
	# domicile = models.CharField(max_length=20)
	# min_followers = models.IntegerField(default=0)
	# desc_photo = models.CharField(max_length=100)
	# example_photo = models.ImageField(upload_to=campaign_img_upload, blank=True)
	# desc_caption = models.CharField(max_length=100)
	# age = models.CharField(max_length=50)


	class Meta:
		model = Campaign
		fields = ['pk', 'author', 'title', 'img', 'description', 'created_at', 'fee', 'gender', 'domicile', 'min_followers', 'desc_photo', 'desc_caption', 'age', 'category', 'periode_start', 'periode_end']
		extra_kwargs = {
			'pk': {'read_only': True},
			'title': {'required': True},
			'description': {'required': True},
			'fee': {'required': True}
		}

	# def __init__(self, *args, **kwargs):
	# 	super(CampaignSerializer, self).__init__(*args, **kwargs)
	# 	if(self.context['request'].user.is_company == False):
	# 		self.fields.pop('paid')
		
class JoinCampaignSerializer(serializers.ModelSerializer):
	campaign_id = serializers.IntegerField()
	author = serializers.CharField(read_only=True)
	paid = serializers.SerializerMethodField(default=False)

	class Meta:
		model = JoinCampaign
		fields = ['pk', 'campaign_id', 'author', 'status', 'draft', 'draft_caption', 'draft_status', 'post', 'paid', 'created_at']
		extra_kwargs = {
			'pk': {'read_only': True},
			'author': {'read_only': True},
			'campaign_id': {'read_only': True},
			'paid' : {'read_only': True},
			'draft': {'read_only': True},
			'post': {'read_only': True},
			'created_at': {'read_only': True},
			'draft_caption': {'required': False}
		}

	# def validate(self, attrs):
		# # if(attrs['valid'])
		# method = self.context['request'].method

		# print(method)
		# if(method == 'POST'):
		# 	campaign = Campaign.objects.get(pk=attrs['campaign_id'])
		# 	print(campaign)
		# 	if(campaign.periode_end < timezone.now()):
		# 		raise serializers.ValidationError({'error': 'campaign telah berakhir'})

		# return attrs


	def get_paid(self, joinCampaign):
		return get_tx_status(joinCampaign)


	def update(self, instance, validated_data):
		# if(validated_data)
		super(JoinCampaignSerializer, self).update(instance, validated_data)
		if 'draft_caption' in validated_data.keys():
			instance.draft_status = 2
			instance.save() 

		return instance

	# def update(self, instance, validated_data):
	# 	popped = validated_data.pop('user', None)
	# 	try:
	# 		no_telepon = popped['no_telepon']
	# 	except:
	# 		no_telepon = None

	# 	try:
	# 		domicile = popped['domicile']
	# 	except:
	# 		domicile = None

	# 	super(InfluenzerSerializer, self).update(instance, validated_data)
	# 	if no_telepon is not None:
	# 		instance.user.no_telepon = no_telepon
	# 		instance.user.save(update_fields=('no_telepon',))

	# 	if  domicile is not None:
	# 		instance.user.domicile = domicile
	# 		instance.user.save(update_fields=('domicile',))

	# 	return instance

	def validate(self, attrs):
		method = self.context['request'].method

		if(method == "PATCH"):
			instance = getattr(self, 'instance', None)

			if(not get_tx_status(instance)):
				raise serializers.ValidationError({"error": "Company belum membayar"})

		return attrs



	def create(self, data):

		try:
			data["campaign_id"] = Campaign.objects.get(pk=data["campaign_id"])
		except:
			raise serializers.ValidationError({"error": "campaign_id tidak valids"})

		joinCampaign = JoinCampaign.objects.filter(campaign_id=data["campaign_id"], author=self.context['request'].user)

		if(joinCampaign.exists()):
			raise serializers.ValidationError({"error": "kamu sudah mendaftar campaign ini"})

		if(data["campaign_id"].periode_end < timezone.now()):
			raise serializers.ValidationError({'error': 'campaign telah berakhir'})

		joinCampaign = JoinCampaign.objects.create(
				campaign = data["campaign_id"],
				author = self.context['request'].user
			)
		joinCampaign.save()
		return joinCampaign
		

class DraftPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = JoinCampaign
		fields = ['draft']

	def validate(self, attrs):
		instance = getattr(self, 'instance', None)

		try:
			order_id = Payment.objects.get(joinCampaign=instance)
			data = tx_status(order_id)
		except:
			data = False

		if(get_tx_status(instance)):
			raise serializers.ValidationError({"error": "Company belum membayar"})

		if(instance.campaign.periode_end < timezone.now()):
			raise serializers.ValidationError({'error': 'campaign telah berakhir'}) 

		if(instance.status == 1):
			raise serializers.ValidationError({"error": "Masih menunggu hasil seleksi dari company"})
		elif(instance.status == 3):
			raise serializers.ValidationError({"error": "Kamu tidak lolos seleksi"})
		elif(instance.status == 4):
			raise serializers.ValidationError({"error": "Task kamu sudah selesai"})


		return attrs

class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = JoinCampaign
		fields = ['pk', 'post']
		# extra_kwargs = {}

	def validate(self, attrs):

		instance = getattr(self, 'instance', None)

		if(not get_tx_status(instance)):
			raise serializers.ValidationError({"error": "Company belum membayar"})

		if(instance.campaign.periode_end < timezone.now()):
			raise serializers.ValidationError({'error': 'campaign telah berakhir'})

		if(instance.status == 1):
			raise serializers.ValidationError({"error": "Masih menunggu hasil seleksi dari company"})
		elif(instance.status == 3):
			raise serializers.ValidationError({"error": "Kamu tidak lolos seleksi"})
		elif(instance.status == 4):
			raise serializers.ValidationError({"error": "Task kamu sudah selesai"})

		if(instance.draft_status != 4):
			raise serializers.ValidationError({"error": "draft kamu belum diverifikasi"})

		return attrs


class ImgCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Campaign
		fields = ['pk', 'img']


class ExampleCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Campaign
		fields = ['pk', 'example_photo']

