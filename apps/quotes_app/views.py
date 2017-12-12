from django.shortcuts import render,redirect, HttpResponse
from django.contrib import messages
from ..login_reg.models import User
from .models import Quote

def index(request):
    all_quotes = Quote.objects.all()
    all_favorites = User.objects.get(id=request.session['user_id']).faves.all() 
   
    
    all_q = set(all_quotes)
    all_f = set(all_favorites)

    all_q -= all_f

    context = {
        'quotes' : Quote.objects.all(),
        'favorites' : User.objects.get(id=request.session['user_id']).faves.all(), 
        'others' : all_q
    }
    return render(request,'quotes_app/index.html',context)

def logout(request):
    return redirect ('/')
def create(request):
    errors = Quote.objects.quote_validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems(): 
            messages.error(request, error, extra_tags=tag)
        return redirect('/quotes/')
    else:
        user = User.objects.get(id = request.session['user_id'])
        Quote.objects.create(
        author = request.POST['author'],
        message = request.POST['message'],
        user = user)
        # quote_id = request.session['id']
        return redirect ('/quotes/')

def add(request, quote_id):
    Quote.objects.addfavorites(request.session['user_id'], quote_id)
    return redirect ('/quotes/')

def remove(request, quote_id):
    Quote.objects.removefavorites(request.session['user_id'], quote_id)
    return redirect ('/quotes/')

def user(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id)
    }
    return render(request, 'quotes_app/user.html', context)

def clear(request):
    request.session.flush()
    return redirect('/')

# Create your views here.
