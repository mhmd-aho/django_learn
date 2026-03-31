from django.shortcuts import render,redirect
from .forms import UserForm
from .models import User

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def usersList(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
def userById(request,id):
    user = User.objects.get(id = id)
    return render(request, 'user.html', {'user': user})
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/')
        else:
            form = UserForm()
    return render(request, 'register.html', {'form': form})