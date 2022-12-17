from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def index(request):

    all_members = Member.objects.all
    return render(request, 'core/index.html', {'all': all_members})


def mypage(request):
    return render(request, 'core/mypage.html')


def login(request):
    if request.method == "GET":
        return render(request, 'core/login.html')
    elif request.method == "POST":

        
        return render(request, 'core/login.html')


def join(request):
    if request.method == 'POST':
        form = MemberForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            age = request.POST['age']
            email = request.POST['email']
            passwd = request.POST['passwd']

            messages.success(request, ('something worng try again'))
            return render(request, 'core/join.html', {
                'fname': fname,
                'lname': lname,
                'age': age,
                'email': email,
                'passwd': passwd,

            })

        messages.success(
            request, ('Your forms has benn sumbmitted successfully'))

        return redirect('index')
    else:
        return render(request, 'core/join.html')
