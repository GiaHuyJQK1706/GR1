# Generated by Django 5.0.1 on 2024-03-15 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_payment_completed_order_payment_method'),
        ('products', '0008_alter_review_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='order_item',
            field=models.ForeignKey(limit_choices_to={'order__status': 'Delivered'}, on_delete=django.db.models.deletion.CASCADE, to='orders.orderitem'),
        ),
    ]