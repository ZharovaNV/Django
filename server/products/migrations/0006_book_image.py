# Generated by Django 2.1.4 on 2018-12-23 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('products', '0005_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='images.Image'),
        ),
    ]
