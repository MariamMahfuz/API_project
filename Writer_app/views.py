from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def Writer_list(request):
    writers=Profile.objects.all()
    context={
        'writers':writers,
    }
    return render(request,'Writer_Profile/Writer_list.html',context)

    
def Add_writer(request):
    Writer = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Writer has been listed")
    context={
        'Writer':Writer
    }
    return render(request,'Writer_Profile/Add_Writer.html',context)


def Writer_Profile(request,primarykey):
    writer_details=Profile.objects.get(pk=primarykey)
    context={
        'writer_details':writer_details
    }
    return render(request,'Writer_Profile/Profile.html',context)

def Edit_Profile(request,primarykey):
    writer_details=Profile.objects.get(pk=primarykey)
    edit_form = ProfileForm(instance=writer_details)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=writer_details)
        if form.is_valid():
            form.save()
            
    context={
        'edit_form':edit_form,
    }
    return render(request,'Writer_Profile/Edit_Profile.html',context)

def Delete_profile(request, primarykey):
    writer_details = Profile.objects.get(pk=primarykey)
    if request.method == "POST":
        writer_details.delete()
        messages.success(request, "Object has been deleted")
    context = {
        'writer_details' : writer_details
    }
    return render(request,'Writer_Profile/Delete_Profile.html',context)