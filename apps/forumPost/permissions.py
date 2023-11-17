from rest_framework import permissions

class ValidUserOfPostUpdate(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        methods = ['PUT','DELETE']
        if request.method in methods:
            return request.user.id == obj.user.id

        return True