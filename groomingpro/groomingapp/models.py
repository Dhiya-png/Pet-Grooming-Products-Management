from django.db import models

# Create your models here.

class registration(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=60)
    password=models.CharField(max_length=30)
    cpassword=models.CharField(max_length=30)

# booking informations

class bookinginfo(models.Model):
    user=models.ForeignKey(registration,on_delete=models.CASCADE)
    petname=models.CharField(max_length=30)
    breed=models.CharField(max_length=20)
    age=models.IntegerField()
    petgender=models.CharField(max_length=20)

    def __str__(self):
        return self.petname



# packages uploading

class packages(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=40)
    price=models.IntegerField()
    service=models.CharField(max_length=600)


# _________________________________________________________________________________________________________

# pet products section

class productsupload_model(models.Model):
    image=models.ImageField(upload_to='images/')
    proname=models.CharField(max_length=40)
    desc=models.CharField(max_length=100)
    proprice=models.IntegerField()
    category=models.CharField(max_length=40)

# add to cart section
class cartmodel(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(productsupload_model,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

# wishlist

class wishlistmodel(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(productsupload_model,on_delete=models.CASCADE)


#address details for buying products
class address_details_model(models.Model):
     user_details=models.ForeignKey(registration,on_delete=models.CASCADE)
     address=models.CharField(max_length=50)
     roadname=models.CharField(max_length=40)
     pincode=models.IntegerField()
     city=models.CharField(max_length=40)
     state=models.CharField(max_length=40)
     contact_person=models.CharField(max_length=40)
     contact_num=models.IntegerField()


# order details
class ordermodel(models.Model):
    userdetails=models.ForeignKey(registration,on_delete=models.CASCADE)
    address=models.ForeignKey(address_details_model,on_delete=models.CASCADE)
    order_date=models.DateTimeField(auto_now_add=True)

class orderitemmodel(models.Model):
    Order=models.ForeignKey(ordermodel,on_delete=models.CASCADE)
    orderpic=models.ImageField(upload_to='images/')
    pro_name=models.CharField(max_length=20)
    order_price=models.IntegerField()
    pro_quantity=models.CharField(max_length=20)


class contact(models.Model):
    email=models.EmailField(max_length=40)
    msg=models.CharField(max_length=100)

# gallary
class gallary(models.Model):
    image=models.ImageField(upload_to='images/')
