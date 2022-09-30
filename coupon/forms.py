from django import forms
from tempus_dominus.widgets import DateTimePicker
from coupon.models import Coupon


class ApplyCouponForm(forms.Form):
    code = forms.CharField()

    class Meta:
        model = Coupon
        fields = ['code']

    def __init__(self, *args, **kwargs):
        super(ApplyCouponForm, self).__init__(*args, **kwargs)
        self.fields['code'].label = ""


class CouponForm(forms.ModelForm):

    class Meta:
        model = Coupon
        fields = ('code', 'valid_from', 'valid_to', 'discount', 'active')

    def __init__(self, *args, **kwargs):
        super(CouponForm, self).__init__(*args, **kwargs)
        self.fields['code'].label = "Promotion Code "
        self.fields['valid_from'].label = "Valid From  "
        self.fields['valid_to'].label = "Valid To  "
        self.fields['discount'].label = "Promotion Amount "
        self.fields['valid_from'].widget.attrs['class'] = \
            'form-control datetimepicker-input'
        self.fields['valid_from'].widget = DateTimePicker()
        self.fields['valid_to'].widget.attrs['class'] = \
            'form-control datetimepicker-input'
        self.fields['valid_to'].widget = DateTimePicker()
