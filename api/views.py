from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin
from .models import Project, Bug, Comment, Request, Notification
from .serializers import ProjectSerializer, GetProjectSerializer, BugSerializer, CreateBugSerializer, UpdateBugSerializer, CommentSerializer, RequestSerializer, GetRequestSerializer, NotificationSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
import datetime
from django.utils import timezone as tz


from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from django.core.exceptions import PermissionDenied

from django.contrib.auth import get_user_model
from core.serializers import UserSerializer

class GroupRequiredMixin(object):
    """
        group_required - list of strings, required param
    """

    group_required = None

    def dispatch(self, request, *args, **kwargs):
        req = self.initialize_request(request, *args, **kwargs)

        if req.method not in ["POST", "PUT", "PATCH", "DELETE"]:
            return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)
    
        if not req.user.is_authenticated:
            raise PermissionDenied
        else:
            user_groups = []
            for group in req.user.groups.values_list('name', flat=True):
                user_groups.append(group)
            if len(set(user_groups).intersection(self.group_required)) <= 0:
                raise PermissionDenied
        return super(GroupRequiredMixin, self).dispatch(request, *args, **kwargs)


class MemberBugsViewSet(ModelViewSet):
    serializer_class = BugSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Bug.objects.filter(member=user).select_related("member").prefetch_related("comments")


class ProjectViewSet(GroupRequiredMixin, ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    group_required = [u'Admin', u'Manager']

    queryset = Project.objects.all().prefetch_related('members')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetProjectSerializer
        return ProjectSerializer


class BugViewSet(GroupRequiredMixin, ModelViewSet):
    # serializer_class = BugSerializer

    group_required = [u'Admin', u'Manager', u'Developer']

    def get_queryset(self):
        return Bug.objects.filter(project_id=self.kwargs['project_pk']).select_related('member').prefetch_related('comments')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateBugSerializer
        elif self.request.method == 'PUT':
            return UpdateBugSerializer
        return BugSerializer

    def get_serializer_context(self):
        return {'project_id': self.kwargs['project_pk']}


# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer

#     def get_queryset(self):
#         return Comment.objects.filter(project_id=self.kwargs['project_pk'])
    
#     def get_serializer_context(self):
#         return {'project_id': self.kwargs['project_pk']}


class CommentViewSet(GroupRequiredMixin, ModelViewSet):
    group_required = [u'Admin', u'Manager', u'Developer', u'Viewer']
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class RequestViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]
    
    queryset = Request.objects.all().select_related('member')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return GetRequestSerializer
        return RequestSerializer


class NotificationViewSet(ModelViewSet):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]

    queryset = Notification.objects.filter(created__gt= tz.now() - datetime.timedelta(days=30))
    serializer_class = NotificationSerializer


class AllUsersViewSet(
                  RetrieveModelMixin,
                  ListModelMixin,
                  GenericViewSet):
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]
            
    User = get_user_model()
    queryset = User.objects.all().prefetch_related("groups")
    serializer_class = UserSerializer