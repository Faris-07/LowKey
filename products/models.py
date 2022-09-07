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

