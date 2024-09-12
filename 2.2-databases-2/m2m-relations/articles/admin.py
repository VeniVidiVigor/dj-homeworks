from django.contrib import admin

from .models import Article, Tag, Scope


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    list_filter = ['published_at']
    inlines = [ScopeInline,]


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
