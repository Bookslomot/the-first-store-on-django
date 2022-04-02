from django.contrib import admin
from django.utils.safestring import mark_safe

from shop.models import Product, Category, Subcategory, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_now', 'quantity', 'status', 'cat', 'get_image', )
    list_display_links = ('name', 'get_image', )
    search_fields = ('name', 'cat__name')
    list_filter = ('status', 'discount', 'cat', )
    ordering = ('name', )
    readonly_fields = ('get_image', )
    raw_id_fields = ['cat', ]
    list_editable = ('status', )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="150" height="100"')

    get_image.short_description = 'Фото товара'


class ReviewProductsInCategory(admin.TabularInline):
    model = Product
    extra = 0
    readonly_fields = ('name', 'description', 'price_now', 'price_old', 'quantity', 'photo', 'status', 'discount', 'slug', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ReviewProductsInCategory]
    save_on_top = True


# class ReviewProductInSubcategory(admin.TabularInline):
#     model =
#     extra = 0
#     readonly_fields = ('name', 'description', 'price_now', 'price_old', 'quantity', 'photo', 'status', 'discount', 'slug', )


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    pass
    # inlines = [ReviewProductInSubcategory]
    # save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'created_at')
    list_filter = ('active',)
    ordering = ('-created_at',)


admin.site.site_title = 'Администрирование Магазина'
admin.site.site_header = 'Администрирование Магазина'