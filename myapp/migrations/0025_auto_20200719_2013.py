# Generated by Django 3.0.8 on 2020-07-19 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_auto_20200719_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Product_detail',
            field=models.CharField(max_length=200, null=True),
        ),
    ]