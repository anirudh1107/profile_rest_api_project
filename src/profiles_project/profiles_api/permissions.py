from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is trying to edit thier own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class PostOwnStatus(permissions.BasePermission):
    """checks if user is updating his own status"""

    def has_object_permission(self, request, view, obj):
        """checks the user to update their own status"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user.profile.id == request.user.id
