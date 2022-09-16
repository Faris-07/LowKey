from django.db import models

# Create your models here.

class Category(models.Model):
    """ category model """
    class Meta:
        """ override plural name """
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=50)
    name_to_display = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ programmatic name """
        return self.category_name

    def get_name_to_display(self):
        """ return name to display on site """
        return self.name_to_display


product_size_choices = (
    ("S", "S"),
    ("M", "M"),
    ("L", "L"),
    ("XL", "XL"),
)

class Product(models.Model):
    name = models.CharField(max_length=254)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=2, choices=product_size_choices, default="M")
    composition = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
