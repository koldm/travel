from csv import list_dialects
from django.contrib import admin
from .models import Category, Tag, PopularTag, Article, Comment


class ArticleCategoryAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'name', 'is_active', 'url',)
  list_display_links = ('id', 'name', 'is_active', 'url',)
  list_filter = ('is_active',)
  prepopulated_fields = {'url': ('name',)}
  readonly_fields = ('count_articles',)
  fieldsets = (
    ('Основные настройки', {
      'fields': (('is_active',), ('depth', 'parent'), ('name', 'url',))
    }),
    ('SEO', {
      'fields': (('title', 'description', 'keywords',), 'text',)
    }),
    ('Изменяем по крону', {
      'fields': ('count_articles',)
    }),
  )


class TagAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'name', 'url', 'is_active', 'date_created', 'status', 'count_articles',)
  list_display_links = ('id', 'name', 'url', 'is_active', 'date_created', 'status', 'count_articles',)
  list_filter = ('is_active', 'status',)
  prepopulated_fields = {'url': ('name',)}
  readonly_fields = ('count_articles',)
  fieldsets = (
    ('Основные настройки', {'fields': ('is_active', ('name', 'url', 'status'),)}),
    ('Изменяем по крону', {'fields': ('count_articles',)}),
  )
  ordering = ('-date_created',)


class PopularTagAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'category', 'tag',)
  list_display_links = ('id', 'category', 'tag',)
  list_filter = ('category__name',)
  fieldsets = (
    ('Основные настройки', {'fields': (('category', 'tag',),)}),
  )


class ArticleAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'name', 'is_active', 'date_published',)
  list_display_links = ('id', 'name', 'is_active', 'date_published',)
  list_filter = ('is_active', 'category__name',)
  prepopulated_fields = {'url': ('name',)}
  readonly_fields = ('count_comments', 'average_rating',)
  fieldsets = (
    ('Основные настройки', {'fields': (('is_active', 'date_published',), ('name', 'url',), ('category', 'author',),)}),
    ('Текст', {'fields': ('preview_text', 'detail_text',)}),
    ('Дополнительные настройки', {'fields': ('tags',)}),
    ('Изменяем по крону', {'fields': (('count_comments', 'average_rating',),)}),
  )


class CommentAdmin(admin.ModelAdmin):
  artions_on_bottom = True
  list_display = ('id', 'is_active', 'status', 'comment',)
  list_display_links = ('id', 'is_active', 'status', 'comment',)
  list_filter = ('is_active', 'status',)
  fieldsets = (
    ('Основные настройки', {'fields': (('author', 'article', 'is_active', 'status', 'rating',),)}),
    ('Текст', {'fields': ('comment',)}),
  )

admin.site.register(Category, ArticleCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(PopularTag, PopularTagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
