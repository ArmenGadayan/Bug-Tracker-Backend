from django.contrib import admin
from . import models

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']
    list_per_page = 10
    

@admin.register(models.Bug)
class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'project', 'created', 'status']
    list_per_page = 10


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['body', 'created', 'bug']
    list_per_page = 10


@admin.register(models.Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['body', 'created', 'member']
    list_per_page = 10

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['body', 'created']
    list_per_page = 10


admin.site.site_header = 'Bug Tracker Admin'




