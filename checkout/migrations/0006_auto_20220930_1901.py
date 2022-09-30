# Generated by Django 3.2 on 2022-09-30 19:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
        ('checkout', '0005_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupon.coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
