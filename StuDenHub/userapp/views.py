from django.shortcuts import render
from django.http import HttpResponse
from userapp.models import UserRegisterModel
from django.contrib import messages

def index(request):
    return render(request, "index.html")

def Home(request):
    return index(request)

def userlogin(request):
    return render(request, "userloginpage.html")

def userloginaction(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pswd = request.POST.get('password')
        print(email, pswd)
        email_parts = email.split('@')
        if len(email_parts) == 2:
            domain = email_parts[1]
            accepted_domains = ['fdu.edu', 'ucw.edu', 'nyit.edu', 'ubc.edu', 'langara.edu']
            if domain in accepted_domains:
                user = UserRegisterModel.objects.filter(email=email, pswd=pswd)
                if user:
                    return render(request, "user/userhomepage.html")
                else:
                    messages.error(request, "Invalid credentials")
                    return render(request, "userloginpage.html")
            else:
                messages.error(request, "Invalid email domain. Please use a valid email domain.")
                return render(request, "userloginpage.html")
        else:
            messages.error(request, "Invalid email format. Please enter a valid email.")
            return render(request, "userloginpage.html")
    else: 
        return render(request, "userloginpage.html")

def userregisterpage(request):
    return render(request, "userregisterpage.html")

def userregisterAction(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pswd = request.POST.get('pswd')
        confirm_pswd = request.POST.get('confirm_pswd')
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        studentid = request.POST.get('studentid')
        university = request.POST.get('university')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        print(email, pswd, confirm_pswd, username, mobile, studentid, university, city, state, country) 
        
        email_parts = email.split('@')
        if len(email_parts) == 2:
            domain = email_parts[1]
            accepted_domains = ['fdu.edu', 'ucw.edu', 'nyit.edu', 'ubc.edu', 'langara.edu']
            if domain in accepted_domains:
                if pswd == confirm_pswd:
                    try:
                        rslts = UserRegisterModel.objects.create(email=email, pswd=pswd, username=username, mobile=mobile, studentid=studentid, university=university, city=city, state=state, country=country)
                        if rslts is None:
                            messages.success(request, 'Email ID already exist, Registration Failed ')
                        else:
                            messages.success(request, 'Registration Success')
                    except:
                        messages.success(request, 'Email ID already exist, Registration Failed ')
                        return render(request, 'userregisterpage.html', {})
                else:
                    messages.success(request, 'Password and confirm password not match')
            else:
                messages.success(request, 'Invalid email domain. Please use a valid email domain.')
        else:
            messages.success(request, 'Invalid email format. Please enter a valid email.')
    return render(request, 'userregisterpage.html', {})


def adminlogin(request):
    return render(request, "adminloginpage.html")

def adminloginaction(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pswd = request.POST.get('password')
        print(email, pswd)
        if email == "Admin" and pswd == "Admin":
            return render(request, "admin/adminhomepage.html")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "adminloginpage.html")
    else: 
        return render(request, "adminloginpage.html")