from django.contrib import admin
from article.models import Article

# Register your models here.

# The following line registers the "Article" model to the admin

admin.site.register(Article)
