from django.contrib import admin
from .models import AttractionType, Attraction, AttractionReview, AttractionFaq
from geo.models import City


class AttractionTypeAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'name', 'is_active', 'url',)
  list_display_links = ('id', 'name', 'is_active', 'url',)
  list_filter = ('is_active',)
  prepopulated_fields = {'url': ('name',)}
  fieldsets = (
    ('Основные данные', {
      'fields': ('is_active', ('name', 'url'),)
    }),
  )


class CityFilter(admin.SimpleListFilter):
    title = 'Город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
      region_id = request.GET.get('region__id__exact', None)
      
      if (region_id):
        cities = City.objects.filter(region = region_id)
      else:
        cities = City.objects.filter(region=None)
      return [(city.id, city.name) for city in cities]
    
    def queryset(self, request, queryset):
      city = request.GET.get('city', None)
      if (city):
        return queryset.filter(city__id=city)
      else:
        return queryset.all()


class AttractionAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  readonly_fields = ('average_rating', 'count_reviews',)
  list_display = ('id', 'name', 'is_active', 'url',)
  list_display_links = ('id', 'name', 'is_active', 'url',)
  list_filter = ('is_active', 'types', 'region', CityFilter,)
  prepopulated_fields = {'url': ('name',)}
  fieldsets = (
    (
      'Основные данные', {
        'fields': ('is_active', ('name', 'url',), ('region', 'city',), ('types', )) #+ координаты
      }
    ),
    (
      'SEO', {
        'fields': ('title', 'description', 'keywords',)
      }
    ),
    (
      'Описание', {
        'fields': ('preview_text', 'detail_text',)
      }
    ),
    (
      'Изменяем по крону', {
        'fields': (('average_rating', 'count_reviews',),)
      }
    )
    # photos
  )


class AttractionReviewAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'author', 'status',)
  list_display_links = ('id', 'author', 'status',)
  list_filter = ('status',)
  fieldsets = (
    (
      'Основные данные', {
        'fields': (('status', 'rating', 'author',), 'review', 'attraction',)
      }
    ),
  )


class AttractionFaqAdmin(admin.ModelAdmin):
  actions_on_bottom = True
  list_display = ('id', 'status',)
  list_display_links = ('id', 'status',)
  list_filter = ('status',)
  fieldsets = (
    (
      'Основные настройки', {
        'fields': (('status', 'attraction'),)
      }
    ),
    (
      'Вопрос/Ответ', {
        'fields': (('question', 'answer',), ('author_question', 'author_answer',),)
      }
    ),
  )


admin.site.register(AttractionType, AttractionTypeAdmin)
admin.site.register(Attraction, AttractionAdmin)
admin.site.register(AttractionReview, AttractionReviewAdmin)
admin.site.register(AttractionFaq, AttractionFaqAdmin)
