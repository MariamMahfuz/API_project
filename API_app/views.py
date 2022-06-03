from multiprocessing import context
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == "POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        message=request.POST.get('message')
        message_ins=Message(
            name=name,
            address=address,
            message=message
        )
        message_ins.save()
    messages=Message.objects.all()
    dict={'messages':messages}
    return render(request,'Form/form.html',context=dict)

def edit(request,primaryk):
    message_info=Message.objects.get(pk=primaryk)
    if request.method == "POST":
        name=request.POST.get('name')
        address=request.POST.get('address')
        message=request.POST.get('message')
        message_info.name=name
        message_info.address=address
        message_info.message=message        
        message_info.save()

    context={
        'message_info':message_info
        }
    return render(request,'Form/Edit.html',context)

def delete(request,pk):
    message_info=Message.objects.get(id=pk)
    if request.method == "POST":        
        message_info.delete()
        messages.success(request, "Object has been deleted")
        # print(messages)
        # return redirect('/')
    context={
        'message_info':message_info
    }
    return render(request,'Form/Delete.html',context)

    