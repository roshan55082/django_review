# Generated by Django 3.0.8 on 2020-07-04 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_admin_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='Product_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]