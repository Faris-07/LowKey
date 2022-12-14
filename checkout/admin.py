from django.contrib import admin
from .models import Order, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    """ allows admin to add/edit order items in the admin panel """
    model = OrderItem
    readonly_fields = ('orderitem_total',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order model admin """
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 'delivery_cost',
                       'order_total', 'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'order_date', 'full_name',
              'email', 'phone_number', 'street_address1', 'street_address2',
              'town_city', 'county', 'country', 'postcode', 'coupon',
              'delivery_cost', 'order_total', 'grand_total',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'full_name', 'phone_number',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    # displays most recent orders on the top
    ordering = ('-order_date',)
