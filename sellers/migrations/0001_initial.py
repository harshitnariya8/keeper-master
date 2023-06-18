# Generated by Django 4.1.5 on 2023-02-25 09:19

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AllCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_img', models.ImageField(default='default.jpg', upload_to='cat_image/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_disc', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('seller_cr', models.IntegerField()),
                ('is_featured', models.BooleanField(default=False)),
                ('shopname', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='products/sellers/')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('product_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('shopname', models.CharField(max_length=50, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('categories_list', models.TextField(default='[]', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shop_image', models.ImageField(default='default.jpg', upload_to='sellers_image/<django.db.models.fields.CharField>/')),
                ('total_stars', models.IntegerField(default=0)),
                ('total_reviews', models.IntegerField(default=0)),
                ('avarage_review', models.FloatField(default=0.0)),
                ('credentials', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]