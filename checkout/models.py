import uuid
from decimal import Decimal
from django.db import models
from django.conf import settings
from django.db.models import Sum
from django.core.validators import MinValueValidator, MaxValueValidator

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile
from coupon.models import Coupon


class Order(models.Model):
    """ order model """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name="orders")
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    town_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    order_date = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(Coupon, related_name='orders',
                               null=True, blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')

    def _generate_order_number(self):
        """ generate a random, unique order number """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Updates total cost each time an order item is added """
        if self.discount == 0:
            self.order_total = self.orderitems.aggregate(
                Sum('orderitem_total'))['orderitem_total__sum'] or 0
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            self.grand_total = self.order_total + self.delivery_cost
            self.save()

        else:
            discount_as_decimal = Decimal(self.discount / 100)
            total = self.orderitems.aggregate(Sum('orderitem_total'))['orderitem_total__sum']
            discount = total * discount_as_decimal
            self.order_total = total - discount
            self.delivery_cost = total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            self.grand_total = self.order_total + self.delivery_cost
            self.save()


    def full_address(self):
        """ return address """
        return (f"{self.street_address1}, {self.street_address2}, "
                f"{self.town_city}, {self.county}, {self.postcode}")

    def save(self, *args, **kwargs):
        """ if the order doesn't have an order number, create one """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """ individual items in order """
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='orderitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(
        null=False, blank=False, default=0)
    orderitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False,
        blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the item total
        and update the order total.
        """
        self.orderitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
