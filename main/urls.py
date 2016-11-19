from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^student_profile/$', views.student_profile, name='student_profile'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^student_dept_detail/$', views.student_dept_detail, name='student_dept_detail'),
    url(r'^student_lab_detail/$', views.student_lab_detail, name='student_lab_detail'),
    url(r'^caretaker_profile/$', views.caretaker_profile, name='caretaker_profile'),
    url(r'^warden_profile/$', views.warden_profile, name='warden_profile'),
    url(r'^faculty_profile/$', views.faculty_profile, name='faculty_profile'),
    url(r'^gymkhana_profile/$', views.gymkhana_profile, name='gymkhana_profile'),
    url(r'^account_profile/$', views.account_profile, name='account_profile'),
    url(r'^hod_profile/$', views.hod_profile, name='hod_profile'),
    url(r'^cc_profile/$', views.cc_profile, name='cc_profile'),
    url(r'^onlinecc_profile/$', views.onlinecc_profile, name='onlinecc_profile'),
    url(r'^thesis_manager_profile/$', views.thesis_manager_profile, name='thesis_manager_profile'),
    url(r'^library_profile/$', views.library_profile, name='library_profile'),
    url(r'^lab_profile/$', views.lab_profile, name='lab_profile'),
    url(r'^assistant_registrar_profile/$', views.assistant_registrar_profile, name='assistant_registrar_profile'),

]