from django.db import models
# Create your models here.
from django.utils.html import format_html

from onlinestoreapp.utils import get_image_filename


class Shop(models.Model):
    title = models.CharField(max_length=250, help_text='Shop Name', verbose_name='Shop Name')
    description = models.CharField(max_length=500, help_text='Shop Description', verbose_name='Shop Description')
    image_url = models.URLField(max_length=300, help_text='Shop Picture', verbose_name='Shop Picture')
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Shops"

    def __str__(self):
        return self.title

    def image(self):
        return format_html(
            '<img src="{}" width="100px"/>',
            self.image_url,
            )

    image.short_description = u'Shop Picture'


class Product(models.Model):
    title = models.CharField(max_length=250, help_text="Product Name", verbose_name="Product Name")
    description = models.CharField(max_length=500, help_text='Product Description', verbose_name='Product Description')
    amount = models.IntegerField(default=0)
    price = models.FloatField()
    active = models.BooleanField(default=True)
    categories = models.ManyToManyField('Category', related_name='categories', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def image(self):
        first_image = ProductImage.objects.filter(product=self.id).first()
        return format_html(
            '<img src="{}" width="100px"/>',
            first_image.image.url,
            )

    def get_categories(self):
        return ",".join([str(category.title) for category in self.categories.all()])

    image.short_description = u'Product Picture'
    get_categories.short_description = u'Categories'


class ProductImage(models.Model):
    image = models.ImageField(upload_to=get_image_filename)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Category Name', verbose_name='Category Name')
    description = models.CharField(max_length=500, help_text='Category Description',
                                   verbose_name='Category Description')
    parent = models.ManyToManyField("self", symmetrical=False, blank=True, related_name='sub_categories')

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def get_parents(self):
        return ", ".join([str(pts.title) for pts in self.sub_categories.all().exclude(id=self.id)])

    get_parents.short_description = 'Sub-Categories'
