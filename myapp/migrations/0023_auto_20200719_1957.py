# Generated by Django 3.0.8 on 2020-07-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_auto_20200719_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Product_detail',
            field=models.CharField(default='Oops! Product Details Are Not Vailable', max_length=200, null=True),
        ),
    ]
