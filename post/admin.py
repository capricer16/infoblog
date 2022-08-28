from django.contrib import admin
from post.models import Post, Comments, Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Category)