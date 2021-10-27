from rest_framework.permissions import BasePermission

# class CampaignDetailPermission(BasePermission):

# 	def has_object_permission(self, request, view, obj):
# 		if (request.method == "PATCH" or request.method == "DELETE"):
# 			return (obj.author == request.user)
# 		elif (request.method == "GET"):
# 			return (request.user.is_company == False)
# 		elif

class IsOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		return (obj.author == request.user)

class IsPostAndCompany(BasePermission):

	def has_permission(self, request, view):
		if (request.method == "POST"):
			return (request.user.is_company == True)

		return True


class IsPatchDeleteAndOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if (request.method == "PATCH" or request.method == "DELETE"):
			return (obj.author == request.user)

		return True

class IsGetAndInfluenzer(BasePermission):

	def has_permission(self, request, view):
		print(request.user.is_company == False)
		if(request.method == "GET"):
			return (request.user.is_company == False)

		return True

class IsPostAndInfluenzer(BasePermission):

	def has_permission(self, request, view):
		print(request.user.is_company == False)
		if(request.method == "POST"):
			return (request.user.is_company == False)

		return True

class IsCompanyAndOwner(BasePermission):

	def has_object_permission(self, request, view, obj):
		if(request.user.is_company == True):
			return (obj.author == request.user)

		return True