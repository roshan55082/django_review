# Generated by Django 3.0.8 on 2020-07-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200704_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='Product_image',
            field=models.ImageField(blank=True, default='image/default.jpg', upload_to='image/'),
        ),
    ]
