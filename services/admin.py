from django.contrib import admin
from .models import Service, Menu

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServiceAdmin)
admin.site.register(Menu, MenuAdmin)