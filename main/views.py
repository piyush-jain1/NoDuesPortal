from django.http import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.db.models import Q
from .forms import UserForm




def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        # print str(role)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                role = str(role)
                username=request.user.username
                username = str(username)
                if role == "Student":
                    students = Student.objects.all()
                    
                    flag=0
                    for stud in students:
                        if stud.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/student_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})

                elif role == "Faculty":
                    faculty = Faculty.objects.all()
                    flag=0
                    for fac in faculty:
                        if fac.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/faculty_profile')   
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                    
                elif role == "Lab":
                    labs = Lab.objects.all()
                    flag=0
                    for lab in labs:
                        if lab.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/lab_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})

                elif role == "Caretaker":
                    caretaker = Caretaker.objects.all()
                    flag=0
                    for care in caretaker:
                        if care.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/caretaker_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})

                elif role == "Warden":
                    warden = Warden.objects.all()
                    flag=0
                    for ward in warden:
                        if ward.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/warden_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})

                elif role == "Gymkhana":
                    gymkhana = Gymkhana.objects.all()
                    flag=0
                    for gym in gymkhana:
                        if gym.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/gymkhana_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                   
                elif role == "OnlineCC":
                    onlinecc = OnlineCC.objects.all()
                    flag=0
                    for onl in onlinecc:
                        if onl.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/onlinecc_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                   
                elif role == "CC":
                    cc = CC.objects.all()
                    flag=0
                    for c in cc:
                        if c.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('cc_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                   
                elif role == "Thesis Manager":
                    thesis = SubmitThesis.objects.all()
                    flag=0
                    for thes in thesis:
                        if thes.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/thesis_manager_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                    
                elif role == "Library":
                    library = Library.objects.all()
                    flag=0
                    for lib in library:
                        if lib.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/library_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                    
                elif role == "Assistant Registrar":
                    asst = asstreg.objects.all()
                    flag=0
                    for a in asst:
                        if a.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/assistant_registrar_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                    
                elif role == "HOD":
                    hod = HOD.objects.all()
                    flag=0
                    for h in hod:
                        if h.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/hod_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})
                
                elif role == "Account":
                    account = Account.objects.all()
                    flag=0
                    for acc in account:
                        if acc.webmail == username:
                            flag=1
                    if flag==1:
                        return redirect('/account_profile')
                    else:
                        return render(request, 'main/login.html', {'error_message': 'Invalid Role'})

                else:
                    return render(request, 'main/login.html', {'error_message': 'Invalid Credentials'})

            else:
                return render(request, 'main/login.html', {'error_message': 'Invalid Credentials'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Invalid Credentials'})
    return render(request, 'main/login.html',{'error_message': 'Valid Login'})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'main/login.html', context)


def student_profile(request):
    username=request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    return render(request, 'main/student.html',{'error_message': 'valid login', 'student': student})


def student_dept_detail(request):
    username=request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    faculty_dept = Faculty.objects.filter(dept=student.dept)
    stud_fac_status = StudFacStatus.objects.filter(student=student)
    return render(request,'main/student_dept_detail.html',{'error_message': 'valid login','student': student, 'faculty':faculty_dept, 'StudFacStatus': stud_fac_status})


def student_lab_detail(request):
    username = request.user.username
    username = str(username)
    student = Student.objects.get(webmail=username)
    labs = Lab.objects.all()
    stud_lab_status = StudLabStatus.objects.filter(student=student)
    return render(request, 'main/student_lab_detail.html', {'error_message': 'valid login', 'student': student, 'labs' : labs, 'StudLabStatus':stud_lab_status})


def account_profile(request):
    if request.method == "GET":
        username = request.user.username
        account = Account.objects.get(webmail=username)
        students = Student.objects.filter(hod_approval=True)
        return render(request, 'main/account.html',
                      {'error_message': 'valid login', 'students': students,
                       'account': account})
    elif request.method == "POST":
        username = request.user.username
        account = Account.objects.get(webmail=username)
        students = Student.objects.filter(hod_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.account_approval = True
                stud.save()
            else:
                stud.account_approval = False
                stud.save()
        return redirect('/account_profile',{'error_message': 'valid login', 'students': students,'account': account})


def assistant_registrar_profile(request):
    if request.method == "GET":
        username = request.user.username
        assistant_registrar= asstreg.objects.get(webmail=username)
        students = Student.objects.filter(caretaker_approval=True,warden_approval=True,gymkhana_approval=True)
        return render(request, 'main/assistant_registrar.html',
                      {'error_message': 'valid login', 'students': students, 'assistant_registrar': assistant_registrar})
    elif request.method == "POST":
        username = request.user.username
        assistant_registrar= asstreg.objects.get(webmail=username)
        students = Student.objects.filter(caretaker_approval=True, warden_approval=True, gymkhana_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.assistant_registrar_approval = True
                stud.save()
            else:
                stud.assistant_registrar_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/assistant_registrar_profile',{'students': students, 'assistant_registrar': assistant_registrar})


def caretaker_profile(request):
    if request.method == "GET":
        username = request.user.username
        caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = Student.objects.filter(hostel=hostel)
        return render(request, 'main/caretaker.html',
                      {'error_message': 'valid login', 'students': students, 'caretaker': caretaker, 'hostel': hostel})
    elif request.method=="POST":
        username = request.user.username
        caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = Student.objects.filter(hostel=hostel)
        for stud in students:
            if request.POST.get(stud.webmail,"") == 'on':
                stud.caretaker_approval=True
                stud.save()
            else :
                stud.caretaker_approval = False
                stud.warden_approval = False
                stud.assistant_registrar_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/caretaker_profile',{ 'students': students, 'caretaker': caretaker, 'hostel': hostel })


def onlinecc_profile(request):
    if request.method == "GET":
        username = request.user.username
        onlinecc = OnlineCC.objects.get(webmail=username)
        students = Student.objects.all()
        return render(request, 'main/onlinecc.html',
                      {'error_message': 'valid login', 'students': students, 'onlinecc': onlinecc})
    elif request.method == "POST":
        username = request.user.username
        onlinecc = OnlineCC.objects.get(webmail=username)
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.online_cc_approval = True
                stud.save()
            else:
                stud.online_cc_approval = False
                stud.cc_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/onlinecc_profile',{'students': students, 'onlinecc': onlinecc})

def cc_profile(request):
    if request.method == "GET":
        username = request.user.username
        cc = CC.objects.get(webmail=username)
        students = Student.objects.filter(online_cc_approval=True)
        return render(request, 'main/cc.html',
                      {'error_message': 'valid login', 'students': students, 'cc': cc})
    elif request.method == "POST":
        username = request.user.username
        cc = CC.objects.get(webmail=username)
        students = Student.objects.filter(online_cc_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.cc_approval = True
                stud.save()
            else:
                stud.cc_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/cc_profile',{'students': students, 'cc': cc})


def faculty_profile(request):
    if request.method == "GET":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.dept
        students = Student.objects.filter(dept=dept)
        stud_fac_status = StudFacStatus.objects.filter(faculty=fac)
        return render(request, 'main/faculty.html',
                      {'error_message': 'valid login', 'students': students, 'faculty': fac, 'dept': dept,'StudFacStatus': stud_fac_status})
        
    elif request.method=="POST":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.dept
        students = Student.objects.filter(dept=dept)
        stud_fac_status = StudFacStatus.objects.filter(faculty=fac)
        for stud in students:
            for i in stud_fac_status :
                if i.student.name == stud.name:
                    if request.POST.get(stud.webmail,"") == 'on':
                        x=StudFacStatus.objects.get(student=stud, faculty=fac)
                        x.approval=True
                        x.save()
                        
                    else :
                        x = StudFacStatus.objects.get(student=stud, faculty=fac)
                        print x
                        x.approval=False
                        x.save()
                        stud.dept_status = False
                        stud.hod_approval = False
                        stud.account_approval = False
                        stud.save()
        return redirect('/faculty_profile',{'students': students, 'faculty': fac, 'dept':dept,'StudFacStatus': stud_fac_status})


def gymkhana_profile(request):
    if request.method == "GET":
        username = request.user.username
        gymkhana = Gymkhana.objects.get(webmail=username)
        students = Student.objects.all()
        return render(request, 'main/gymkhana.html',
                      {'error_message': 'valid login', 'students': students, 'gymkhana': gymkhana})
    elif request.method == "POST":
        username = request.user.username
        gymkhana = Gymkhana.objects.get(webmail=username)
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.gymkhana_approval = True
                stud.save()
            else:
                stud.gymkhana_approval = False
                stud.assistant_registrar_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/gymkhana_profile',{'students': students, 'gymkhana': gymkhana})
        

def hod_profile(request):
    if request.method == "GET":
        username = request.user.username
        hod = HOD.objects.get(webmail=username)
        students = Student.objects.filter(dept=hod.dept, assistant_registrar_approval=True,library_approval=True, cc_approval=True)
        return render(request, 'main/hod.html',
                      {'error_message': 'valid login', 'students': students,
                       'hod': hod})
    elif request.method == "POST":
        username = request.user.username
        hod = HOD.objects.get(webmail=username)
        students = Student.objects.filter(dept=hod.dept, assistant_registrar_approval=True,library_approval=True, cc_approval=True)
        for stud in students:
            if stud.lab_status() == True and stud.dept_status() == True:
                if request.POST.get(stud.webmail, "") == 'on':
                    stud.hod_approval = True
                    stud.save()
                else:
                    stud.hod_approval = False
                    stud.account_approval = False
                    stud.save()
        return redirect('/hod_profile',{'error_message': 'valid login', 'students': students,'hod': hod})

        
def lab_profile(request):
    if request.method == "GET":
        username = request.user.username
        lab = Lab.objects.get(webmail=username)
        students = Student.objects.all()
        stud_lab_status = StudLabStatus.objects.filter(lab=lab)
        return render(request, 'main/lab.html',
                      {'error_message': 'valid login', 'students': students, 'lab': lab, 'StudLabStatus': stud_lab_status})
    elif request.method=="POST":
        username = request.user.username
        lab = Lab.objects.get(webmail=username)
        students = Student.objects.all()
        stud_lab_status = StudLabStatus.objects.filter(lab=lab)
        for stud in students:
            for i in stud_lab_status :
                if i.student.name == stud.name:
                    if request.POST.get(stud.webmail,"") == 'on':
                        x=StudLabStatus.objects.get(student=stud, lab=lab)
                        x.approval=True
                        x.save()
                    else :
                        x = StudLabStatus.objects.get(student=stud, lab=lab)
                        x.approval=False
                        x.save()
                        stud.lab_status = False
                        stud.hod_approval = False
                        stud.account_approval = False
                        stud.save()
        return redirect('/lab_profile',{'students': students, 'lab': lab, 'StudLabStatus': stud_lab_status})


def library_profile(request):
    if request.method == "GET":
        username = request.user.username
        library = Library.objects.get(webmail=username)
        students = Student.objects.filter(submit_thesis=True)
        return render(request, 'main/library.html',
                      {'error_message': 'valid login', 'students': students, 'library': library})
    elif request.method == "POST":
        username = request.user.username
        library = Library.objects.get(webmail=username)
        students = Student.objects.filter(submit_thesis=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.library_approval = True
                stud.save()
            else:
                stud.library_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/library_profile',{'students': students, 'library': library})




def thesis_manager_profile(request):
    if request.method == "GET":
        username = request.user.username
        thesis_manager = SubmitThesis.objects.get(webmail=username)
        students = Student.objects.all()
        return render(request, 'main/thesis_manager.html',
                      {'error_message': 'valid login', 'students': students, 'thesis_manager':thesis_manager})
    elif request.method == "POST":
        username = request.user.username
        thesis_manager = SubmitThesis.objects.get(webmail=username)
        students = Student.objects.all()
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.submit_thesis = True
                stud.save()
            else:
                stud.submit_thesis = False
                stud.library_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/thesis_manager_profile',{'students': students, 'thesis_manager':thesis_manager})


def warden_profile(request):
    if request.method == "GET":
        username = request.user.username
        warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = Student.objects.filter(hostel=hostel, caretaker_approval=True)
        return render(request, 'main/warden.html',
                      {'error_message': 'valid login', 'students': students, 'warden': warden,
                       'hostel': hostel})
    elif request.method == "POST":
        username = request.user.username
        warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = Student.objects.filter(hostel=hostel, caretaker_approval=True)
        for stud in students:
            if request.POST.get(stud.webmail, "") == 'on':
                stud.warden_approval = True
                stud.save()
            else:
                stud.warden_approval = False
                stud.assistant_registrar_approval = False
                stud.hod_approval = False
                stud.account_approval = False
                stud.save()
        return redirect('/warden_profile', {'students': students, 'warden': warden,
                       'hostel': hostel })



def rules(request):
    return render(request,'main/rules.html')

def contact(request):
    return render(request,'main/contact.html')



