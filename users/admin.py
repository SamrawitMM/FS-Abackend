from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm #CustomUserCreationForm
    add_form = CustomUserCreationForm
    # fieldsets = (
    #     *UserAdmin.fieldsets,
    #     (
    #         'User Type',
    #         {
    #             'fields':(
    #                 'user_type' ,
    #                 # 'is_driver',
    #                 # 'is_owner',
    #             )
    #         },
           
            
    #     ),
    #     (
    #         'Personal Details',
    #         {
    #             'fields':(
    #                 'full_name' ,
    #                 'phone_number',
    #                 # 'is_owner',
    #             )
    #         },
           
            
    #     ),
    # )
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('user_type',)}),('Personal Details', {'fields': ('phone_number',)})
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Type', {'fields': ('user_type',)}),('Personal Details', {'fields': ('phone_number',)})
    )


  
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
