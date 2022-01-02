from django.contrib import admin
from .models import Article, Sport


admin.site.register(Sport)
admin.site.register(Article)