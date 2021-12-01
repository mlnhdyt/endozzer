from rest_framework import serializers

from .models import *

class InfluenzerSerializer(serializers.ModelSerializer):
	user_id = serializers.IntegerField()
	no_telepon = serializers.CharField(source='user.no_telepon', required=False)
	domicile = serializers.CharField(source='user.domicile', required=False)

	class Meta:
		fields = ('user_id', 'domicile', 'no_telepon', 'birth_date', 'gender', 'instagram', 'tiktok', 'balance')
		model = Influenzer
		extra_kwargs = {
			'user_id': {'required': False},
			'domicile': {'required': False},
			'no_telepon': {'required': False},
			'birth_date': {'required': True},
			'gender': {'required': True},
			'instagram': {'required': False},
			'tiktok': {'required': False},
			'balance': {'read_only': True}
		}

	def update(self, instance, validated_data):
		popped = validated_data.pop('user', None)
		try:
			no_telepon = popped['no_telepon']
		except:
			no_telepon = None

		try:
			domicile = popped['domicile']
		except:
			domicile = None

		super(InfluenzerSerializer, self).update(instance, validated_data)
		if no_telepon is not None:
			instance.user.no_telepon = no_telepon
			instance.user.save(update_fields=('no_telepon',))

		if  domicile is not None:
			instance.user.domicile = domicile
			instance.user.save(update_fields=('domicile',))

		return instance


class CompanySerializer(serializers.ModelSerializer):
	user_id = serializers.IntegerField()
	no_telepon = serializers.CharField(source='user.no_telepon', required=False)
	domicile = serializers.CharField(source='user.domicile', required=False)

	class Meta:
		model = Company
		fields = ('user_id', 'no_telepon', 'domicile', 'brand', 'address')

	def update(self, instance, validated_data):
		popped = validated_data.pop('user', None)
		try:
			no_telepon = popped['no_telepon']
		except:
			no_telepon = None

		try:
			domicile = popped['domicile']
		except:
			domicile = None

		super(CompanySerializer, self).update(instance, validated_data)
		if no_telepon is not None:
			instance.user.no_telepon = no_telepon
			instance.user.save(update_fields=('no_telepon',))

		if  domicile is not None:
			instance.user.domicile = domicile
			instance.user.save(update_fields=('domicile',))

		return instance


	# def get_no_telepon(self, influenzer):
	# 	return influenzer.user.no_telepon

	# def update_no_telepon(self, influenzer):
	# 	influenzer.user.no_telepon



	# def validate(self, attrs):
	# 	method = self.context['request'].method
	# 	if(method == "GET"):
	# 		instance = getattr(self, 'instance', None)
	# 		attrs['no_telepon'] = instance.user.no_telepon



# class InfluenzerSerializer(serializers.ModelSerializer):
# 	first_name = serializers.CharField(source='user.first_name')
# 	last_name = serializers.CharField(source='user.last_name')
# 	no_telepon = serializers.CharField(source='user.no_telepon')

# 	class Meta:
# 		fields = ('first_name', 'last_name', 'birth_date', 'no_telepon', 'domicile', 'gender', 'instagram', 'tiktok')
# 		model = Influenzer
# 		extra_kwargs = {
# 			'first_name': {'write_only': True},
# 			'last_name': {'write_only': True},
# 			'first_name': {'write_only': True},

# 		}


