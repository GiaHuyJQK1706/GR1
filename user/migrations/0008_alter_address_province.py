# Generated by Django 5.0.1 on 2024-03-09 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(choices=[('Koshi Province', 'Koshi Province'), ('Madesh Province', 'Madesh Province'), ('Bagmati Province', 'Bagmati Province'), ('Gandaki Province', 'Gandaki Province'), ('Lumbini Province', 'Lumbini Province'), ('Karnali Province', 'Karnali Province'), ('Sudurpashchim Province', 'Sudurpashchim Province')], max_length=100),
        ),
    ]
