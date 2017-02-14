from django.shortcuts import redirect, render

# Create your views here.
def facebook(request):
    return redirect('https://www.facebook.com/MenyuBrasil/')

def index(request):
    return render (request, 'home/angular.html', {})
