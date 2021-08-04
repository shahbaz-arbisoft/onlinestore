from django.utils.text import slugify


def get_image_filename(instance, filename):
    title = instance.product.title
    slug = slugify(title)
    return "product_images/%s-%s" % (slug, filename)
