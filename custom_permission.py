from rest_framework.permissions import BasePermission,SAFE_METHODS

class Custom_Permission(BasePermission):

    def has_permission(self, request, obj):
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):
        
        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.user_register==request.user
        