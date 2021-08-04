from django.contrib import admin

from onlinestoreapp.models import Shop, ProductImage, Product, Category


# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'product']
    list_filter = ('title',)
    search_fields = ['title']
    fields = ['title', 'description', 'image_url', 'product']
    ordering = ['title']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    exclude = ('categories',)
    list_display = ['title', 'description', 'amount', 'price', 'active', 'image', 'get_categories']
    list_filter = ('active', 'price')
    filter_horizontal = ('categories',)
    search_fields = ['id', 'title']
    fields = ['title', 'description', 'amount', 'price', 'active', 'categories']
    ordering = ('amount', 'price',)

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)
        try:
            min_price, max_price = list(map(int, search_term.split('-')))
        except:
            pass
        else:
            if isinstance(min_price, int) and isinstance(max_price, int):
                queryset |= self.model.objects.filter(price__gte=min_price, price__lte=max_price)
        return queryset, use_distinct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'get_parents']
    search_fields = ['title', 'parent__title']
    fields = ['title', 'description', 'parent']
    filter_horizontal = ('parent',)


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
