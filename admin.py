from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'mobile', 'is_staff')
#     search_fields = ('email', 'mobile')
#     ordering = ('email',)

# admin.site.register(CustomUser, CustomUserAdmin)


admin.site.register(User)