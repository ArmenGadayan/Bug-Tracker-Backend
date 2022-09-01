from django.db import models
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="projects", null=True, blank=True)
    #members = models.ManyToManyField(Member, related_name="projects", null=True, blank=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="projects", null=True, blank=True)

    def __str__(self):
        return self.title


class Bug(models.Model): 
    STATUS_IN_PROGRESS = 'In Progress'
    STATUS_RESOLVED = 'Resolved'
    STATUS_NEW = 'New'
    STATUS_ADDITIONAL_INFO_REQUIRED = 'Additional Info Required'
    
    STATUS_CHOICES = [
        (STATUS_NEW, 'New'),
        (STATUS_IN_PROGRESS, 'In Progress'),
        (STATUS_RESOLVED, 'Resolved'),
        (STATUS_ADDITIONAL_INFO_REQUIRED, 'Additional Info Required')
    ]

    TYPE_BUG = 'Bug'
    TYPE_FEATURE_REQUEST = 'Feature Request'
    TYPE_OTHER = 'Other'

    TYPE_CHOICES = [
        (TYPE_BUG, 'Bug'),
        (TYPE_FEATURE_REQUEST, 'Feature Request'),
        (TYPE_OTHER, 'Other')
    ]

    PRIORITY_LOW = 'Low'
    PRIORITY_MEDIUM = 'Medium'
    PRIORITY_HIGH = 'High'

    PRIORITY_CHOICES = [
        (PRIORITY_LOW, 'Low'),
        (PRIORITY_MEDIUM, 'Medium'),
        (PRIORITY_HIGH, 'High')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_NEW)
    type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=TYPE_BUG)
    priority = models.CharField(max_length=7, choices=PRIORITY_CHOICES, default=PRIORITY_LOW)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bug')  
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bugs', null=True)  
    #member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='bugs', null=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bugs', null=True) 

    def __str__(self):
        return self.title


class Comment(models.Model):
    body = models.TextField(max_length=500, null=True, blank=True)
    commenter = models.CharField(max_length=255, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comment', null=True)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return self.body[0:50]


class Request(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='requests', null=True) 

    def __str__(self):
        return self.body[0:50]


class Notification(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.body[0:50]
