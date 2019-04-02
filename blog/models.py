from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# what we want to save to the database

#convention to use (uppercase)'P'ost
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE) #delete the user we delete all the posts

	#how does you want to display the name of object of Post table/class in database or django-ORM
	def __str__(self):
		return str(self.author) + " -- " + self.title

	def snippet(self):
		return self.content[:250] + ' ...'

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})


