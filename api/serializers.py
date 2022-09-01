from rest_framework import serializers
from .models import Project, Bug, Comment, Request, Notification
from core.serializers import UserBaseSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body', 'commenter', 'created', 'bug']


class BugSerializer(serializers.ModelSerializer):
    # member = serializers.SerializerMethodField()

    # def get_member(self, bug: Bug):
    #     return {'id': bug.member.id, "name": f'{bug.member.first_name} {bug.member.last_name}' }
    member = UserBaseSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Bug
        fields = ['id', 'title', 'description', 'updated', 'created', 'status', 'type', 'priority', 'member', 'project', 'comments']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return Bug.objects.create(project_id=project_id, **validated_data)


class CreateBugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['id', 'title', 'description', 'updated', 'created', 'status', 'type', 'priority', 'member']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return Bug.objects.create(project_id=project_id, **validated_data)


class UpdateBugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bug
        fields = ['title', 'description', 'status', 'type', 'priority']

    def create(self, validated_data):
        project_id = self.context['project_id']
        return Bug.objects.create(project_id=project_id, **validated_data)


class ProjectSerializer(serializers.ModelSerializer):
    # members = serializers.SerializerMethodField()

    # def get_members(self, project: Project):
    #         members = {}
    #         for member in project.members.all():
    #             members[member.id] = (f'{member.first_name} {member.last_name}', member.email)
    #         return members

    # def get_members(self, project: Project):
    #         return [f'{member.first_name} {member.last_name}' for member in project.members.all()]

    # members = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created', 'updated', 'members']

class GetProjectSerializer(serializers.ModelSerializer):
    # members = serializers.SerializerMethodField()

    # def get_members(self, project: Project):
    #         members = {}
    #         for member in project.members.all():
    #             members[member.id] = (f'{member.first_name} {member.last_name}', member.email)
    #         return members

    members = UserBaseSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'created', 'updated', 'members']


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = ['id', 'body', 'commenter', 'created']

#     def create(self, validated_data):
#         project_id = self.context['project_id']
#         return Comment.objects.create(project_id=project_id, **validated_data)

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'body', 'created', 'member']


class GetRequestSerializer(serializers.ModelSerializer):
    # member = UserSerializer()

    member = serializers.SerializerMethodField()

    def get_member(self, request: Request):
        return {'first_name': request.member.first_name, "last_name": request.member.last_name, "email": request.member.email}

    class Meta:
        model = Request
        fields = ['id', 'body', 'created', 'member']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'body', 'created']



