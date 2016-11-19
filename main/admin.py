from django.contrib import admin
from .models import *

class StudFacStatusInline(admin.TabularInline):
	model = StudFacStatus
	extra = 1

class StudLabStatusInline(admin.TabularInline):
	model = StudLabStatus
	extra = 1

class StudentAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']
	inlines = (StudFacStatusInline,StudLabStatusInline,)
	filter_horizontal = ('faculty_approval', 'lab_approval',)

class FacultyAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']
	inlines = (StudFacStatusInline,)


class CaretakerAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']

class WardenAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']

class GymkhanaAdmin(admin.ModelAdmin):
	list_display = ('name',)

class LibraryAdmin(admin.ModelAdmin):
	list_display = ('name',)

class OnlineCCAdmin(admin.ModelAdmin):
	list_display = ('name',)

class SubmitThesisAdmin(admin.ModelAdmin):
	list_display = ('name',)

class LabAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']
	inlines = (StudLabStatusInline,)

class CCAdmin(admin.ModelAdmin):
	list_display = ('name',)

class asstregAdmin(admin.ModelAdmin):
	list_display = ('name',)

class HODAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_field = ['name']

class AccountAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
admin.site.register(Student,StudentAdmin)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Caretaker,CaretakerAdmin)
admin.site.register(Warden,WardenAdmin)
admin.site.register(Gymkhana,GymkhanaAdmin)
admin.site.register(Library,LibraryAdmin)
admin.site.register(Lab,LabAdmin)
admin.site.register(CC,CCAdmin)
admin.site.register(asstreg,asstregAdmin)
admin.site.register(HOD,HODAdmin)
admin.site.register(Account,AccountAdmin)
admin.site.register(OnlineCC,OnlineCCAdmin)
admin.site.register(SubmitThesis,SubmitThesisAdmin)
