from django.contrib import admin
from .models import Blog, Comment, Album, Track


admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Album)
admin.site.register(Track)