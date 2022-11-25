# TODO здесь производится настройка пермишенов для нашего проекта
from django.http import Http404
from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

from ads.models import Ad
from users.models import User


class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsAdminOrOwner(permissions.BasePermission):

    def has_object_permission(self, *args):
        is_owner = IsOwner().has_object_permission(*args)

        #convert tuple to list
        new_args = list(args)
        #remove object for non-object permission args
        new_args.pop()
        is_admin = IsAdminUser().has_permission(*new_args)

        return is_owner or is_admin


class AdUpdatePermission(permissions.BasePermission):
    message = 'Managing others ads not permitted'

    def has_permission(self, request, view):
        if request.user.role in [User.IsOwner, User.IsAdmin]:
            return True
        try:
            entity = Ad.objects.get(pk=view.kwargs["pk"])
        except Ad.DoesNotExist:
            raise Http404

        if entity.owner_id == request.user.id:
            return True
        return False
