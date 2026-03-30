from django.shortcuts import render
from .forms import UserForm

# Create your views here.
from django.http import HttpResponse, HttpResponseNotFound

def index(request): 
    greet = "<h1 style='color: red;'>Hello,i'm mohamad abou hamoud</h1>"
    return HttpResponse(greet)
def greet(request,id):
    users = {
        '12':"mohamad abou hamoud from saida",
        '23':"bassam rekab from syria",
        '34':"mhmd shndr from tripoli",
    } 
    return HttpResponse(f"""
    <h1>Hello, {id}</h1>
    <p>{users[id]}</p>
    """)
def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
             form.save()
    return render(request, 'register.html', {'form': form})