from django.urls import path
from.views import *
urlpatterns=[
    path('sellerindex/',seller_index),
    path('sellerreg/',register),
    path('seller_login/',seller_login),
    path('seller_profile/',seller_profile),
    path('pro_upload/',product),
    path('packagesupload/',packageupload),
    path('photo_upload/',photos)


]