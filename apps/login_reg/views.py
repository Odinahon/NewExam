from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from .models import User

def index(request):
    return render(request,'login_reg/index.html')

# Create your views here.
def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['name']=result.name
    request.session['alias']=result.alias
    messages.success(request, "Successfully registered!")
    return redirect('/quotes')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    request.session['name']=result.name
    request.session['alias']=result.alias
    messages.success(request, "Successfully logged in!")
    return redirect('/quotes')