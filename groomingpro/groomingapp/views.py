from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.conf import settings
import stripe
from datetime import datetime,timedelta
from .models import bookinginfo
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail




# Create your views here.

def index(request):
    return render(request,'index.html')

def reg(request):
    if(request.method=='POST'):
        fnm=request.POST.get('firstname')
        lnm=request.POST.get('lastname')
        email=request.POST.get('email')
        add=request.POST.get('address')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if(password==cpassword):
            db=registration(first_name=fnm,last_name=lnm,email=email,address=add,phone=phone,password=password)
            db. save()
            return redirect(login)
        else:
            return HttpResponse('failed')

    return render(request,'register.html')

# login page
def login(request):
    if(request.method=="POST"):
        email=request.POST.get('email')
        password=request.POST.get('password')
        db=registration.objects.all()
        for i in db:
             if(i.email==email and i.password==password):
                 request.session['userid'] =i.id
                 return redirect(index)
        else:
                 return HttpResponse('login failed')
    return render(request,'login.html')


# userprofile

def profile(request):
    id1=request.session['userid']
    db= registration.objects.get(id=id1)
    return render(request,'profile.html',{'data':db})


# profile edit

# update profile
# booking page
def updateprofile(request):
    id1=request.session['userid']
    db=registration.objects.get(id=id1)
    if(request.method=="POST"):
        db.image=request.FILES.get('image')
        db.name=request.POST.get('name')
        db.email=request.POST.get('email')
        db.phone=request.POST.get('phone')
        db.save()
        return redirect(profile)
    return render(request,'update_profile.html',{'data':db})





# _____________________________________________________
# upload packages
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




def packdisplay(request):
    db=packages.objects.all()
    return render(request,'packages_display.html',{'data':db})

def booking(request):
    id1=request.session['userid']
    userdata=registration.objects.get(id=id1)
    if(request.method=="POST"):
        petname=request.POST.get('petname')
        breed=request.POST.get('breed')
        age=request.POST.get('age')
        petgender=request.POST.get('petgender')
        db=bookinginfo(user=userdata,petname=petname,breed=breed,age=age,petgender=petgender)
        db.save()

        return redirect(index)

    return render(request,'booking.html')

# __________________________________________________________________________________________________________

# pet product section


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


def prodislay(request):
    id1=request.session['userid']
    db=registration.objects.get(id=id1)
    category=request.GET.get('category')
    x=productsupload_model.objects.all()
    if(category==category):
        return render(request,'pro_display.html',{'data':db,'x':x})

# cart
def addtocart(request,itemid):
    item=productsupload_model.objects.get(id=itemid)
    cart=cartmodel.objects.all()
    for i in cart:
        if(i.item.id==itemid  and i.userid==request.session['userid']):
            i.quantity+=1
            i.save()
            return redirect(cartdisplay)
    else:
        db=cartmodel(userid=request.session['userid'],item=item)
        db.save()
    return redirect(cartdisplay)


def cartdisplay(request):
    id1=request.session['userid']
    db=cartmodel.objects.filter(userid=id1)
    total=0
    count=0
    for i in db:
        i.item.proprice*=i.quantity
        total+=i.item.proprice
        count+=1
    return render(request,'cartdisplay.html',{'data':db,'total':total,'count':count})


# quantity increment and decrement

def incdec(request,cartid):
    db=cartmodel.objects.get(id=cartid)
    action=request.GET.get('action')
    if(action=='increment'):
        db.quantity+=1
        db.save()
    elif action=='decrement' and db.quantity>1:
            db.quantity-=1
            db.save()
    return redirect(cartdisplay)

# remove

def removecart(request,cartid):# Redirect to cartdisplay view after deletion
    db=cartmodel.objects.get(id=cartid)
    action=request.GET.get('action')
    if(action=='remove'):
        db.delete()
    return redirect(cartdisplay)




# wishlist

# adding to wishlist
def addtowish(request,itemid):
    item=productsupload_model.objects.get(id=itemid)
    wish=wishlistmodel.objects.all()
    for i in wish:
        if(i.item.id==itemid and i.userid==request.session['userid']):
            i.save()
            return HttpResponse('item already in wishlist')
    else:
        db=wishlistmodel(userid=request.session['userid'],item=item)
        db.save()
        return redirect(wishlist)

def wishlist(request):
    db=wishlistmodel.objects.all()
    total=0
    count=0
    for i in db:
        total+=i.item.proprice
        count+=1
    return render(request,'wishlist.html',{'data':db,'total':total,'count':count})

# wishlist item remove
def wishremove(requet,wishitem):
    db=wishlistmodel.objects.get(id=wishitem)
    action=requet.GET.get('action')
    if(action=='remove'):
        db.delete()
    return redirect(wishlist)

# delivery details
def address(request):
    id1=request.session['userid']
    userdata=registration.objects.get(id=id1)
    if(request.method=="POST"):
        address=request.POST.get('address')
        roadname=request.POST.get('roadname')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        state=request.POST.get('state')
        contact_person=request.POST.get('contact_person')
        contact_num=request.POST.get('contact_num')
        db=address_details_model(user_details=userdata,address=address,roadname=roadname,pincode=pincode,
                                 city=city,state=state,contact_person=contact_person,contact_num=contact_num)
        db.save()
        return redirect(delivery)
    return render(request,'address.html')

# delivery address
def delivery(request):
    userid=request.session['userid']
    db=address_details_model.objects.filter(user_details__id=userid)
    return render(request,'delivery.html',{'data':db})

# product summary

def product_summary(request):
    userid=request.session['userid']
    address_id=request.GET.get('address')

    address=address_details_model.objects.get(id=address_id)
    cartitems=cartmodel.objects.filter(userid=userid)
    key=settings.STRIPE_PUBLISHABLE_KEY
    total=0
    striptotal=0
    for i in cartitems:
        i.item.proprice*=i.quantity
        total+=i.item.proprice
        striptotal=total*100
    return render(request,'product_summary.html',{'address':address,'cartitems':cartitems,
                                          'total':total,'key':key,'striptotal':striptotal})


# order details
def create_order(request):  #after payment
    if(request.method=="POST"):
        order_item = []
        total_price = 0
        userid=request.session['userid']    #usser session calling
        user=registration.objects.get(id=userid)    #register deteails
        address_id=request.POST.get('address_id')  #hidden fieled addres id
        address=address_details_model.objects.get(id=address_id)   #fetch addresss using the address
        cart=cartmodel.objects.filter(userid=userid) #cart filter

#create the order object
        order=ordermodel.objects.create(userdetails=user,address=address)
#cart itration
        for i in cart:
#create order item for each cart item
            orderitemmodel.objects.create(Order=order,orderpic=i.item.image,pro_name=i.item.proname,
                                       pro_quantity=i.quantity,order_price=i.item.proprice)
            total_price+=i.item.proprice*i.quantity   #mail kk illa ata
            order_item.append({
                    'product':i.item.proname,
                    'quantity':i.quantity,
                    'price':i.item.proprice*i.quantity
                })

            #calculating expected delivery date(eg : 7 days from toady )
        expected_delivery_date=datetime.now()+timedelta(days=7)

            #construct email content
        subject='order confirmation'

        context={'order_item':order_item,'total_price':total_price,
                     'expected_delivery_date':expected_delivery_date.strftime('%y-%m%d')}

        html_message=render_to_string('order_confirmation_email.html',context)
        plain_messages=strip_tags(html_message)

        from_email='dhiyararadhakrishnan2002@gmail.com'
        to_email=[user.email]


            #send mail
        send_mail(subject,plain_messages,from_email,to_email,html_message=html_message)

        # cart item delete
        cart.delete()
    return HttpResponse('ordered created successfully')
# orderview
def order_view(request):
    userid =request.session['userid']  # Assuming the user is logged in
    order = orderitemmodel.objects.filter(Order__userdetails__id=userid).order_by('-Order__order_date')
    return render(request, 'order.html', {'order': order})

def ordercancel(request,id):
    userid=request.session['userid']
    user=registration.objects.get(id=userid)
    db=orderitemmodel.objects.get(id=id)
    db.orderstatus=False
    db.save()
    subject='your order is cancelled'
    context={'product':db.pro_name,'price':db.pro_price,'quantity':db.quantity}
    html_message=render_to_string('order_cancellation.html',context)
    plain_message=strip_tags(html_message)
    from_email='dhiyaradhakrishnan2002@gmail.com'
    to_email=[user.email]
    send_mail(subject,plain_message,from_email,to_email,html_message=html_message)
    return HttpResponse('order cancelled')



# about
def about(request):
    return render(request,'about.html')

# contactus
def contact(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        msg = request.POST.get('msg')

        # You can process the form data here, such as sending an email
        if email and msg:
            return HttpResponse('message send succssfully')
    return render(request,'contact.html')

# gallary
def photos(request):
    if(request.method=="POST"):
        image=request.POST.get('photo')
        db=gallary(image=image)
        db.save()
        return HttpResponse('okey')
    return render(request,'gallary_upload.html')

def photodisplay(request):
    db=gallary.objects.all()
    return render(request,'photodisplay.html',{'data':db})





def logout(request):
    request.session.flush()
    return redirect(index)
