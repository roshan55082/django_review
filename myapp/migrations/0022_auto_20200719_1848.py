# Generated by Django 3.0.8 on 2020-07-19 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_sub_reviews_rply_user_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_reviews',
            name='Rply_user_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Admin'),
        ),
    ]
