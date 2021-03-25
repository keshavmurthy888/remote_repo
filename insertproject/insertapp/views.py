from django.shortcuts import render
from insertapp.models import *
# Create your views here.

def insert_details(request):
	student_1=Student_Detail.objects.get_or_create(NAME='HYDER',USN=11223345,PHONE_NUMBER=12121212,EMAIL='abc_3@gmail.com',GENDER='MALE')
	#student_1.save()
	return render(request, 'insertapp/index.html')