from django.contrib import admin

# Register your models here.
from .models import Post
from .models import User
class UserAdmin(admin.ModelAdmin):
    list_display = ('mn','detial')
class PostAdmin(admin.ModelAdmin):
    list_display = ('mn','collect_time','create_time','do','temp','cod','cond','ph','nh3','tp','orp','zd')
admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
