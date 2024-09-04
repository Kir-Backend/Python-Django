from django.contrib import admin, messages
from .models import Man, Person, Category

class MarriedFilter(admin.SimpleListFilter):
    title = "Окольцованность"
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Женат'),
            ('single', 'Не женат'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(wife__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(wife__isnull=True)

@admin.register(Man)
class ManAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'cat', 'wife', 'tags', 'content']
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, man: Man):
        return f'Описание {len (man.content)} символов'

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Man.Status.PUBLISHED)
        self.message_user(request, f'Опубликовано {count} записей.')

    @admin.action(description='Скрыть выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Man.Status.DRAFT)
        self.message_user(request, f'Скрыто {count} записей.', messages.WARNING)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
# Register your models here.
