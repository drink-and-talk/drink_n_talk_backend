from django.contrib import admin

from drink_n_talk.core.models import Bar, Drink, Language, Theme


class DrinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'degree', 'users')
    search_fields = ('title')
    list_filter = ('degree')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'users')
    search_fields = ('name')


admin.site.register(Bar, Theme)
