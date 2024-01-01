from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Message

def ContactView(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        text=request.POST['text']
        new_message=Message.objects.create(name=name,email=email,text=text)
        new_message.save()
        messages.success(request,"Xabar yetkazildi!")
        return redirect('home_page')
    return render(request,'message/contact.html')