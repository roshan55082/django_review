# Generated by Django 3.0.8 on 2020-07-15 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_details_product_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Product_detail',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
