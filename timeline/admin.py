from django.contrib import admin
from .models import Post,Like,ProductModel

admin.site.register(Post)
admin.site.register(ProductModel)
admin.site.register(Like)
# Register your models here.
