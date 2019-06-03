from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    pass
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)