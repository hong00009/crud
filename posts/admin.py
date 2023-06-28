from django.contrib import admin
from .models import Post
# 나의 models.py 안의 Post class
# Register your models here.


admin.site.register(Post)
# admin 사이트에 Post class를 등록