from django.contrib import admin

from .models import NGOProfile, User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'is_staff', 'is_superuser')
    search_fields = ('first_name', 'last_name', 'email', 'role')
    list_filter = ('role', 'is_staff', 'is_superuser')

@admin.register(NGOProfile)
class NGOProfileAdmin(admin.ModelAdmin):
    
    list_display = ('organization_name', 'user', 'approved')
    list_filter = ('approved',)
    search_fields = ('organization_name', 'user_email')
    readonly_fields = ('license_document',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user  # Set user to current logged-in admin
        super().save_model(request, obj, form, change)
    
