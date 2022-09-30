from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from coupon.models import Coupon
from coupon.forms import ApplyCouponForm


def bag_contents(request):
    """ Handles Bag Contents """
    bag_items = []
    total = 0
    product_count = 0
    delivery = 0

    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for item_size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': item_size,
                })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    apply_coupon_form = ApplyCouponForm()
    coupon_id = request.session.get('coupon_id')
    before_coupon = 0
    if coupon_id:
        before_coupon = total
        coupon = Coupon.objects.get(id=coupon_id)
        discount_as_decimal = Decimal(coupon.discount / 100)
        discount = total * discount_as_decimal
        total = total - discount
    else:
        coupon = ''
        discount = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'apply_coupon_form': apply_coupon_form,
        'coupon': coupon,
        'before_coupon': before_coupon,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
