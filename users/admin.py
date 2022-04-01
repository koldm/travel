from django.contrib import admin

from .models import User, UserGuide, UserGuidePhoto, UserGuideCertificate


class UserAdmin(admin.ModelAdmin):
    model = User
    action_on_bottom = True
    list_display = ('id', 'email', 'is_active', 'is_superuser', 'is_staff', 'is_guide', 'is_travel_company',)
    list_display_links = ('id', 'email', 'is_active', 'is_superuser', 'is_staff', 'is_guide', 'is_travel_company',)
    list_filter = ('is_active', 'is_superuser', 'is_staff', 'is_guide', 'is_travel_company',)
    readonly_fields = ('date_created', 'date_updated', 'last_login',)
    fieldsets = (
        ('Основные', {'fields': (('email', 'password'), ('name', 'last_name',), ('phone', 'nickname',), 'avatar',)}),
        ('Разрешения', {'fields': (('is_active', 'is_superuser', 'is_staff', 'is_guide', 'is_travel_company',),)}),
        ('Даты', {'fields': (('date_created', 'date_updated', 'last_login',),)}),
    )
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'password1', 'password2'),
    }),
    )
    search_fields = ('email', 'nickname',)
    ordering = ('email',)


class UserGuideAdmin(admin.ModelAdmin):
    action_on_bottom = True
    list_display = ('id', 'user',)
    list_display_links = ('id', 'user',)
    readonly_fields = ('count_excursions', 'count_guided_tours', 'count_reviews', 'average_rating', 'count_articles',)
    fieldsets = (
        ('Основные', {'fields': ('about', 'user',)}),
        ('Изменяем по крону', {'fields': (('count_excursions', 'count_guided_tours', 'count_reviews', 'average_rating', 'count_articles',),)})
    )
    search_fields = ('user__email',)
    ordering = ('user',)


class UserGuidePhotoAdmin(admin.ModelAdmin):
    action_on_bottom = True
    list_display = ('id', 'guide',)
    list_display_links = ('id', 'guide',)
    fieldsets = (
        ('Основные', {'fields': ('guide', ('photo', 'small_photo',), 'description') }),
    )


class UserGuideCertificateAdmin(admin.ModelAdmin):
    action_on_bottom = True
    list_display = ('id', 'guide',)
    list_display_links = ('id', 'guide',)
    fieldsets = (
        ('Основные', {'fields': ('guide', ('certificate', 'small_certificate',), 'description')}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(UserGuide, UserGuideAdmin)
admin.site.register(UserGuidePhoto, UserGuidePhotoAdmin)
admin.site.register(UserGuideCertificate, UserGuideCertificateAdmin)
