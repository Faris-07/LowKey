from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib import messages
from .models import Coupon
from .forms import ApplyCouponForm, CouponForm


@require_POST
def apply_coupon(request):
    """ Function to apply coupon """
    now = timezone.now()
    # Get the apply coupon form from forms.py
    form = ApplyCouponForm(request.POST)
    # Check if form is valid
    if form.is_valid():
        # If form is valid get the code used by user
        code = form.cleaned_data['code']
        # Retrive coupon object
        try:
            coupon = Coupon.objects.get(
                code__iexact=code,
                valid_from__lte=now,
                valid_to__gte=now,
                active=True
                )
            # store coupon id in the users session
            request.session['coupon_id'] = coupon.id
            # Success Message
            messages.success(request, (
                        f"Success! {coupon} coupon applied")
                    )
        # Error Message
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
            messages.error(
                request,
                "Sorry, that coupon does not exist or is no longer valid"
                )
    # Redirect user to bag view
    return redirect('bag_view')
