from django.db import models

# Create your models here.
class Student_Detail(models.Model):
	NAME = models.CharField(max_length=50)
	USN = models.IntegerField(max_length=10)
	PHONE_NUMBER = models.CharField(max_length=10)
	EMAIL = models.EmailField()
	GENDER = models.CharField(max_length=50)

	class Meta:
		verbose_name = "Student_Detail"
		verbose_name_plural = "Student_Details"

	def __str__(self):
		return str((self.NAME,self.PHONE_NUMBER))
    