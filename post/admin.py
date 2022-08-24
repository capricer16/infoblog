from django.contrib import admin
from post.models import Post 
from post.models import Comments
from post.models import Category 
# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Category)