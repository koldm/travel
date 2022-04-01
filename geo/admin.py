from django.contrib import admin
from .models import Region, City

class RegionAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'name', 'is_active', 'url',)
  list_display_links = ('id', 'name', 'is_active', 'url',)
  list_filter = (
    'is_active',
    ('name_pr', admin.EmptyFieldListFilter),
  )
  prepopulated_fields = {'url': ('name',)}
  fieldsets = (
    ('Основные данные', {
      'fields': ('is_active', ('name', 'name_pr'), 'url',)
    }),
  )


class CityAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('name', 'is_active', 'url',)
  list_display_links = ('name', 'is_active', 'url',)
  list_filter = (
    'is_active',
    ('name_pr', admin.EmptyFieldListFilter),
    'region__name'
  )
  prepopulated_fields = {'url': ('name',)}
  fieldsets = (
    ('Основные данные', {
      'fields': ('is_active', ('name', 'name_pr'), 'url', 'region',)
    }),
  )


admin.site.register(Region, RegionAdmin)
admin.site.register(City, CityAdmin)