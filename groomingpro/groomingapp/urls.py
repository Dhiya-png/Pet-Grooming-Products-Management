from .views import *
from django.urls import path

urlpatterns=[
    path('index/',index),
    path('register/',reg),
    path('login/',login),
    path('profile/',profile),
    path('update_profile/',updateprofile),
    path('booking/',booking),
    path('packagesupload/',packageupload),
    path('packagesdisplay/',packdisplay),
    # path('booking_summary/',booking_summary),

    # ____________________________________

    path('pro_upload/',product),
    path('pro_display/',prodislay),
    path('addtocart/<int:itemid>',addtocart),
    path('cartdisplay/',cartdisplay),
    path('incdec/<int:cartid>',incdec),
    path('remove/<int:cartid>',removecart),
    path('addtowish/<int:itemid>',addtowish),
    path('wishlist/',wishlist),
    path('wishremove/<int:wishitem>',wishremove),
    path('address/',address),
    path('delivery/',delivery),
    path('product_summary/',product_summary),
    path('create_order/',create_order),
    path('order/',order_view),
    path('cancel/',ordercancel),
    path('about/',about),
    path('contact/',contact),
    path('photo_upload/',photos),
    path('photodis/',photodisplay),
    path('logout/',logout)

]