from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=60)
	content = models.CharField(max_length=500)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return  '(' + self.author.username + ')  ' + self.title + '--' + self.content + '.'