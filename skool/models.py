from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Faculty(models.Model):
	emp_id = models.PositiveIntegerField(db_index=True)
	name = models.CharField(max_length=64)
	mobile_no = models.CharField(max_length=10,db_index=True)
	qualification = models.CharField(max_length=5)
	email = models. EmailField(max_length=254)
	DOJ = models.DateField()
	DOB = models.DateField()
	salary = models.PositiveIntegerField()

class Department(models.Model):
	name = models.CharField(max_length=64)
	code = models.CharField(max_length=5)
	HOD = models.ForeignKey('Faculty', related_name='hod')

class Student(models.Model):
	roll_no = models.PositiveIntegerField(db_index=True)
	first_name = models.CharField(max_length=64)
	last_name = models.CharField(max_length=64)
	city = models.CharField(max_length=32)
	state = models.CharField(max_length=32)
	standard = models.CharField(max_length=32)
	sem = models.PositiveIntegerField()
	DOA = models.DateField()
	DOB = models.DateField()
	email = models. EmailField(max_length=254)
	mobile = models.CharField(max_length=10,db_index=True)
	department = models.ForeignKey('Department', related_name='department')


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	is_student = models.BooleanField(default=False)
	is_faculty = models.BooleanField(default=False)


	def create_student_profile(sender,**kwargs):
		student_obj =  kwargs['instance']
		try:
			user = User.objects.get(username=student_obj.roll_no)
		except:
			password = str(student_obj.roll_no)+str(student_obj.DOB.strftime('%Y%m%d'))
			user_obj = User.objects.create_user(username=student_obj.roll_no,password=password)
			user_obj.save()
			user_pro,created_profile = UserProfile.objects.get_or_create(user=user_obj,is_student=True)

	def create_faculty_profile(sender,**kwargs):
		faculty_obj =  kwargs['instance']
		try:
			user = User.objects.get(username=faculty_obj.emp_id)
		except:
			password = str(faculty_obj.emp_id)+str(faculty_obj.DOB.strftime('%Y%m%d'))
			user_obj = User.objects.create_user(username=faculty_obj.emp_id,password=password)
			user_obj.save()
			faculty_profile,created_profile = UserProfile.objects.get_or_create(user=user_obj,is_faculty=True)

	post_save.connect(create_student_profile,sender=Student)
	post_save.connect(create_faculty_profile,sender=Faculty)