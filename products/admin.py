from django.contrib import admin

from products.models import *

admin.site.register(SiteUser)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Trainer)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Appointment)
admin.site.register(Contact)
