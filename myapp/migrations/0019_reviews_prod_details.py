# Generated by Django 3.0.8 on 2020-07-15 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20200715_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='Prod_details',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Details'),
        ),
    ]
