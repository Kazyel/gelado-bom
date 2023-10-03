from django.contrib import admin
from .models import Acai, Sorvete, Picole, ShopCartPicole, ShopCartSorvete, ShopCartAcai
# Register your models here.

admin.site.register(Acai)
admin.site.register(Sorvete)
admin.site.register(Picole)
admin.site.register(ShopCartPicole)
admin.site.register(ShopCartSorvete)
admin.site.register(ShopCartAcai)

