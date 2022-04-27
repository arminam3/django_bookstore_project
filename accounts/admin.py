from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm #for create a new user
    form = CustomUserChangeForm #for change user in admin
    model = CustomUser
    fieldsets = UserAdmin.fieldsets +(
        (None, {'fields': ('age',)}),########
    )
    add_fieldsets = UserAdmin.fieldsets +(
        (None, {'fields': ('age',)}),########
    )


admin.site.register(CustomUser, CustomUserAdmin)