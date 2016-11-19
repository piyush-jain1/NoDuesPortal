from django.db import models

# Create your models here.

class Faculty(models.Model):
	name = models.CharField(max_length=250)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)
	dept = models.CharField(max_length=100)
	#approval = models.BooleanField(default=False)

	def __unicode__(self):
		return self.name

class Lab(models.Model):
	name = models.CharField(max_length=250,default="Lab")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=250)
	roll = models.IntegerField(default=0)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)
	dept = models.CharField(max_length=100)
	hostel = models.CharField(max_length=100)
	faculty_approval = models.ManyToManyField(Faculty, through = 'StudFacStatus')
	lab_approval = models.ManyToManyField(Lab, through = 'StudLabStatus')
	caretaker_approval = models.BooleanField(default=False)
	warden_approval = models.BooleanField(default=False)
	gymkhana_approval = models.BooleanField(default=False)
	library_approval = models.BooleanField(default=False)
	online_cc_approval = models.BooleanField(default=False)
	cc_approval = models.BooleanField(default=False)
	assistant_registrar_approval = models.BooleanField(default=False)
	submit_thesis = models.BooleanField(default=False)
	hod_approval = models.BooleanField(default=False)
	account_approval = models.BooleanField(default=False)

	def dept_status(self):
		faculty_dept=Faculty.objects.filter(dept=self.dept)
		dept_status =True
		for fac in faculty_dept:
			status = StudFacStatus.objects.get(faculty=fac, student=self).approval
			if status == False:
				dept_status = False
				break
		return dept_status


	def lab_status(self):
		labs=Lab.objects.all()
		lab_status =True
		for lab in labs:
			status = StudLabStatus.objects.get(lab=lab, student=self).approval
			if status == False:
				lab_status = False
				break
		return lab_status

	def __unicode__(self):
		return self.webmail


class StudFacStatus(models.Model):
	faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	approval = models.BooleanField(default = False)

	def __unicode__(self):
		return self.student.webmail

class StudLabStatus(models.Model):
	lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
	student = models.ForeignKey(Student,on_delete=models.CASCADE)
	approval = models.BooleanField(default = False)

	def __unicode__(self):
		return self.student.webmail

class Caretaker(models.Model):
	name = models.CharField(max_length=250)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)
	hostel = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Warden(models.Model):
	name = models.CharField(max_length=250)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)
	hostel = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Gymkhana(models.Model):
	name = models.CharField(max_length=250,default="Gymkhana")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class Library(models.Model):
	name = models.CharField(max_length=250,default="Library")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class OnlineCC(models.Model):
	name = models.CharField(max_length=250,default="OnlineCC")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class CC(models.Model):
	name = models.CharField(max_length=250,default="CC")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class SubmitThesis(models.Model):
	name = models.CharField(max_length=250,default="Submit Thesis")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class asstreg(models.Model):
	name = models.CharField(max_length=250)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name

class HOD(models.Model):
	name = models.CharField(max_length=250)
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)
	dept = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

class Account(models.Model):
	name = models.CharField(max_length=250,default="Account")
	webmail = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name
