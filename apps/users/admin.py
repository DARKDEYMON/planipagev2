from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
	model = User
	fieldsets = UserAdmin.fieldsets + (
		("Extra", {'fields': ('ci',)}),
	)

admin.site.register(User, CustomUserAdmin)
