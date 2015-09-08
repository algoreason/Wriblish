from django.contrib import admin
from cms.models import Post,Topic
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Post)
admin.site.register(Topic)