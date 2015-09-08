from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
	heading=models.CharField(max_length=200)
	text = models.TextField()
	author = models.ForeignKey('auth.user')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True , null=True)
	topic = models.ForeignKey('Topic')
	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def __str__(self):
		return self.heading

class Topic(models.Model):
	topic_name = models.CharField(max_length=200)
	desc = models.TextField()
	def __str__(self):
		return self.topic_name