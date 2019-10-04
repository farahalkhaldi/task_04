from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name = models.CharField(max_length=105)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	"""docstring for Restaurant"""



	