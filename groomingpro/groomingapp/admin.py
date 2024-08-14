from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(registration)
admin.site.register(bookinginfo)
admin.site.register(packages)

# product section

admin.site.register(productsupload_model)
admin.site.register(cartmodel)
admin.site.register(address_details_model)
admin.site.register(wishlistmodel)
admin.site.register(ordermodel)
admin.site.register(orderitemmodel)
admin.site.register(gallary)
