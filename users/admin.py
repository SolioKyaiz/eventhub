from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","username","first_name","last_name","email")
    list_display_links = ("id","username","first_name","last_name")
    search_fields = ("username",'first_name','last_name','email')
    list_filter = ("is_organizer","is_superuser","is_active")