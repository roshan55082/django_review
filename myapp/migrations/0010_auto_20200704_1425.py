# Generated by Django 3.0.8 on 2020-07-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20200704_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='Product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
