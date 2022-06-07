from django.contrib import admin
from .models import Address, People, Bio, Product, Doctor
# Register your models here.
admin.site.register(People)
admin.site.register(Address)
admin.site.register(Doctor)
admin.site.register(Bio)
admin.site.register(Product)