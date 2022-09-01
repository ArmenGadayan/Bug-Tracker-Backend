from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer
from rest_framework import serializers
from django.conf import settings
from django.contrib.auth.models import Group


class UserCreateSerializer(BaseUserCreateSerializer):
    # role = serializers.SerializerMethodField()

    # def get_role(self, user: settings.AUTH_USER_MODEL):
    #     ROLE_ADMIN = 'Admin'

    #     if user.is_superuser:
    #         return ROLE_ADMIN
    #     return user.role

    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
     )  

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name', 'groups']


class GroupSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Group
        fields = ('name',)

class UserSerializer(BaseUserSerializer):
    groups = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
    )  

    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_first_name(self, user: settings.AUTH_USER_MODEL):
        return user.first_name.capitalize()

    def get_last_name(self, user: settings.AUTH_USER_MODEL):
        return user.last_name.capitalize()

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'groups'] 


class UserBaseSerializer(BaseUserSerializer):
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()

    def get_first_name(self, user: settings.AUTH_USER_MODEL):
        return user.first_name.capitalize()

    def get_last_name(self, user: settings.AUTH_USER_MODEL):
        return user.last_name.capitalize()

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name'] 




