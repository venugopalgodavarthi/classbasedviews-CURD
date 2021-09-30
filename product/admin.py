from django.contrib import admin
from product.models import *
# Register your models here.
class productadmin(admin.ModelAdmin):
    list_display=['pname','pdesc','price','discount','item']
admin.site.register(productmodel,productadmin)

class itemadmin(admin.ModelAdmin):
    list_display=['itemname']
admin.site.register(itemmodel,itemadmin)