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
            name='AllOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('customer_name', models.CharField(default='NA', max_length=100)),
                ('seller_id', models.IntegerField()),
                ('payment_id', models.CharField(max_length=120)),
                ('payment_created_at', models.CharField(blank=True, max_length=120, null=True)),
                ('amount_paid', models.FloatField(blank=True, null=True)),
                ('ttl_amount', models.FloatField(blank=True, null=True)),
                ('amount_due', models.FloatField(blank=True, null=True)),
                ('order_details', models.CharField(max_length=1000)),
                ('is_accepted', models.BooleanField(blank=True, default=None, null=True)),
                ('is_delivered', models.BooleanField(blank=True, default=None, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_rejected', models.BooleanField(blank=True, default=None, null=True)),
                ('order_type', models.CharField(default='HOME_DELIVERY', max_length=50)),
                ('order_status', models.CharField(default='PENDING', max_length=50)),
                ('pickup_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=50)),
                ('banner_photo', models.ImageField(upload_to='banner/')),
                ('prio', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.CharField(max_length=250, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('cus_image', models.ImageField(default='default.jpg', upload_to='customer_image/<django.db.models.fields.CharField>/')),
                ('access_review_to_seller_list', models.TextField(default='[]', max_length=200)),
                ('credentials', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CustAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=250)),
                ('pincode', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
