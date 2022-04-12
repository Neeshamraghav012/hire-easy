from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class JobProfile(models.Model):

	user = models.ForeignKey(User, on_delete = models.CASCADE)

	resume = models.FileField(upload_to = "media/")
	bio = models.TextField()
	linkedin = models.URLField()
	github = models.URLField()
	other_profiles = models.URLField()
	interest = models.TextField()
	experiance = models.CharField(max_length = 1000)


	def __str__(self):
		return self.user.username