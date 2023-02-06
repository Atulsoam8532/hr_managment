from django.shortcuts import render,redirect
from .models import Profiles,eplo_project,Hr_employe,leave_manag,manager_employe
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        uname= request.POST.get('uname')
        passw = request.POST.get('passw')
        opt = request.POST.get('option')
        print(opt)
        make = User.objects.create_user(username = uname,first_name = fname,last_name=lname,email=email,password=passw)
        make.save()
        prof = Profiles.objects.create(user= make,apply_for = opt)
        prof.save()
        return redirect('login')
    return render(request,'first_page.html')


def Login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')
        user = authenticate(username=uname,password=passw)
        if user is not None:
            login(request,user)
            return redirect('main')
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login')

def main(request):
    curent = request.user
    print(curent)
    prof = Profiles.objects.get(user=curent)
    print(prof.is_hr)
    return render(request,'main.html',{'prof':prof})

def profile(request):
    prof = Profiles.objects.get(user=request.user)
    return render(request,'profile.html',{'prof':prof})

def add_proj(request):
    users = User.objects.all()
    prof = Profiles.objects.all()
    profi= Profiles.objects.get(user= request.user)
    if request.method == 'POST':
        pname = request.POST.get('pname')
        stdate = request.POST.get('stdate')
        endate = request.POST.get('endate')
        emp = request.POST.get('employe')
        empo = User.objects.get(username= emp)
        manager = request.POST.get('manag')
        curre = request.POST.get('user')
        print(manager)
        mana = User.objects.get(username = manager)
        pro = eplo_project.objects.create(pro_name = pname,start_date = stdate,end_date = endate,RM = mana,added_by = curre)
        pro.user.add(empo)
        pro.save()
        profil= Profiles.objects.get(user=empo)
        profil.allocated_proj=pname
        profil.save()
        return redirect('main')
    return render(request,'add_project.html',{'users':users,'profi':prof,'prof':profi})


def view_proj(request):
    project = eplo_project.objects.filter(added_by = request.user)
    profil = Profiles.objects.filter(is_employe=True)
    if request.method == 'POST':
        proname = request.POST.get('proname')
        emp = request.POST.get('empl')
        us = User.objects.get(username=emp)
        print(emp)
        addi = eplo_project.objects.get(pro_name=proname)
        addi.employes.add(us)
        alloc = Profiles.objects.get(user=us)
        alloc.allocated_proj=proname
        alloc.save()
        addi.save()
        return redirect('main')
    prof = Profiles.objects.get(user= request.user)
    return render(request,'view_project.html',{'projects':project,'profiles':profil,'prof':prof})

def add_employe(request):
    users = Profiles.objects.all()
    prof = Profiles.objects.get(user=request.user)
    cure = User.objects.get(username = request.user)
    
    if request.method == 'POST':
        hr_emp = request.POST.get('employe')
        hr_empo = User.objects.get(username = hr_emp)
        profi = Profiles.objects.get(user = hr_empo)
        profi.HR = cure.username
        profi.save()
        hr_manag = request.POST.get('manag')
        hr_mana = User.objects.get(username=hr_manag)
        add = Hr_employe.objects.create(empolye = hr_empo,manager=hr_mana)
        add.save()
        profi = Profiles.objects.get(user = hr_mana)
        profi.HR = cure.username
        profi.save()
        return redirect('add_emplo')
    
    return render(request,'add_employe.html',{'users':users,'prof':prof})
def man_emp(request):
    users = Profiles.objects.all()
    prof = Profiles.objects.get(user=request.user)
    cure = User.objects.get(username = request.user)
    if request.method =='POST':
        manage = request.POST.get('manager')
        man_emp = request.POST.get('manemp')
        print(man_emp)
        ma_emp= User.objects.get(username=man_emp)
        pro = Profiles.objects.get(user=ma_emp)
        pro.manager=manage
        pro.save()
        man = manager_employe.objects.create(employe = ma_emp)
        man.save()
        return redirect('main')
    return render(request,'manager_add.html',{'users':users,'prof':prof})
def view_employe(request):
    emplo = Profiles.objects.filter(HR = request.user)
    prof = Profiles.objects.get(user=request.user)
    return render(request,'view_emp.html',{'emplo':emplo,'prof':prof})


def apply_leave(request):
    if request.method == 'POST':
        day= request.POST.get('leave')
        leave = leave_manag.objects.create(days = day,user=request.user)
        leave.save()
        return redirect('main')
    user= leave_manag.objects.filter(user=request.user)
    prof = Profiles.objects.get(user=request.user)
    return render(request,'apply.html',{'prof':prof,'user':user})


def hr_leave_approval(request):
    hr = Profiles.objects.filter(HR= request.user)
    print(hr)
    leave = leave_manag.objects.all()
    print(leave)
    prof = Profiles.objects.get(user=request.user)
    return render(request,'hr_approve_leave.html',{'leave':leave,'hr':hr,'prof':prof})

def manager_leave_approval(request):
    hr = Profiles.objects.filter(manager= request.user)
    print(hr)
    leave = leave_manag.objects.all()
    print(leave)
    prof = Profiles.objects.get(user=request.user)
    return render(request,'manager_approvels.html',{'leave':leave,'hr':hr,'prof':prof})

def hr_leave_approved(request,id):
    leave = leave_manag.objects.get(id=id)
    leave.hr_approved = True
    leave.save()
    return redirect('hr_leave_approval')

def hr_leave_reject(request,id):
    leave = leave_manag.objects.get(id=id)
    leave.hr_reject = True
    leave.save()
    return redirect('hr_leave_approval')

def manager_leave_approved(request,id):
    leave = leave_manag.objects.get(id=id)
    leave.manager_approve = True
    leave.save()
    return redirect('manager_leave_approval')

def manager_leave_reject(request,id):
    leave = leave_manag.objects.get(id=id)
    leave.manager_reject = True
    leave.save()
    return redirect('manager_leave_approval')

def emp_project(request):
    profi = Profiles.objects.get(user=request.user)
    proj = eplo_project.objects.filter(employes= request.user)
    return render(request,'project.html',{'prof':profi,'proj':proj})


def search(request):
    search = request.GET.get('searchs')
    print(search)
    profil = Profiles.objects.filter(user__username__icontains = search)
    prof = Profiles.objects.get(user=request.user)
    return render(request,'search.html',{'result':profil,'prof':prof})


def edit_emp(request,id):
    prof = Profiles.objects.get(user= request.user)
    profile = Profiles.objects.get(id = id)
    us = User.objects.get(username = profile.user)
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        change = User.objects.get(id= id)
        change.first_name = fname
        change.last_name=lname
        change.email = email
        change.save()
        return redirect('main')
    return render(request,'edit_emp.html',{'prof':prof,'us':us,'profile':profile})


def view_emp(request,id):
    prof = Profiles.objects.get(user= request.user)
    profile = Profiles.objects.get(id = id )
    emp = User.objects.get(username = profile.user)
    print(emp)
    return render(request,'view.html',{'prof':prof,'empo':profile,'us':emp})

def manager_emp(request):
    prof = Profiles.objects.get(user=request.user)
    emp = Profiles.objects.filter(manager = request.user)
    return render(request,'manager_view_emp.html',{'prof':prof,'emp':emp})