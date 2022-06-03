from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    user=False
    if request.method=='POST':
        username=request.POST.get('username')
        url='https://api.github.com/users/%s' %username
        response=requests.get(url)
        user=response.json()

    context={
        'user':user,
    }
    return render(request,'index.html',context)