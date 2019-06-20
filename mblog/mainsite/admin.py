from django.contrib import admin
from .models import Post

# Register your models here.
#username:admin psw:273926

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','pub_date')

admin.site.register(Post,PostAdmin)