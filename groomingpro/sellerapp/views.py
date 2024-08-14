from django.shortcuts import render,redirect
from django.http import HttpRequest
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from groomingapp.models import*
from django.contrib.auth.forms import AuthenticationForm

def seller_index(request):
    return render(request,'sellerindex.html')

def register(request):
    if(request.method=="POST"):
        form=regform(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('cpassword')
            if(password!=cpassword):
                messages.error(request,'password incorrect')
            else:
                user=form.save(commit=False)
                user.set_password(password)
                user.save()
                messages.success(request,'registration success')
                return redirect(seller_login)
    else:
        form=regform

    return render(request,'sellerreg.html',{'form':form})


def seller_login(request):
    if(request.method=="POST"):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if(user is not None):
                login(request,user)
                request.session['sellerid']=user.id
                messages.success(request,f'you  are now logged in as {username}')
                return redirect(seller_profile)
            else:
                messages.error(request,'invalid username or password')
        else:
            messages.error(request,'form is not valid')
    else:
        form=AuthenticationForm()
    return render(request,'seller_login.html',{'form':form})



def seller_profile(request):
    id1=request.session['sellerid']
    db=User.objects.get(id=id1)
    return render(request,'seller_profile.html',{'data':db})

# def update_profile(request):


def packageupload(request):
    if(request.method=="POST"):
        image=request.FILES.get('image')
        title=request.POST.get('title')
        price=request.POST.get('price')
        services=request.POST.get('services')
        db=packages(image=image,title=title,price=price,service=services)
        db.save()
        return redirect(packdisplay)
    return render(request,'packages_upload.html')


def product(request):
    if(request.method=="POST"):
        image=request.FILES.get('image')
        pro_name=request.POST.get('pro_name')
        desc=request.POST.get('desc')
        pro_price=request.POST.get('pro_price')
        category=request.POST.get('category')
        db=productsupload_model(image=image,proname=pro_name,desc=desc,proprice=pro_price,category=category)
        db.save()
        return redirect(prodislay)
    return render(request,'products_upload.html')


from django.shortcuts import HttpResponse
def photos(request):
    if(request.method=="POST"):
        image=request.POST.get('gallery')
        db=gallary(image=image)
        db.save()
        return HttpResponse('photo uploaded succesfully')
    return render(request,'gallary_upload.html')