from django.contrib import admin

from blog.models import Article, ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    save_as = True

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)
