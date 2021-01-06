from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # add_form = if we modify the custom model to add new fields
    # form = '' Adding the form according to the model just in case of modifications
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)

