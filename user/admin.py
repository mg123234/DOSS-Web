from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from user.models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

    def has_add_permission(self, request):
        return False
        
class UserAdmin(BaseUserAdmin):
    def has_add_permission(self, request, obj=None):
        return False

admin.site.unregister(User)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(User, UserAdmin)
