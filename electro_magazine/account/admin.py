from django.contrib import admin
from django.utils.safestring import mark_safe

from account.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'created_at', 'updated_at', 'is_active', 'is_staff')
    list_display_links = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username', )
    readonly_fields = ('get_image', )
    save_as = True
    list_editable = ('is_active', 'is_staff')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="100"')

    get_image.short_description = 'Фото профиля '



