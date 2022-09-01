from django.urls import path
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('projects', views.ProjectViewSet, basename='projects')
router.register('member-bugs', views.MemberBugsViewSet, basename='members')

router.register('comments', views.CommentViewSet, basename='comments')

router.register('requests', views.RequestViewSet, basename='requests')
router.register('notifications', views.NotificationViewSet, basename='notifications')

router.register('all-users', views.AllUsersViewSet, basename="users")

bug_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
bug_router.register('bugs', views.BugViewSet, basename='project-bugs')

# router.register('bugs', views.BugViewSet, basename='project-bugs')

# comment_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
# comment_router.register('comments', views.CommentViewSet, basename='project-comments')

urlpatterns = router.urls + bug_router.urls

# comment_router.urls