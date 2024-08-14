# Generated by Django 5.0.7 on 2024-07-21 05:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='address_details_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('roadname', models.CharField(max_length=40)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
                ('state', models.CharField(max_length=40)),
                ('contact_person', models.CharField(max_length=40)),
                ('contact_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=40)),
                ('msg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='gallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='packages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('service', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='productsupload_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('proname', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=100)),
                ('proprice', models.IntegerField()),
                ('category', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ordermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.address_details_model')),
                ('userdetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.registration')),
            ],
        ),
        migrations.CreateModel(
            name='orderitemmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderpic', models.ImageField(upload_to='images/')),
                ('pro_name', models.CharField(max_length=20)),
                ('order_price', models.IntegerField()),
                ('pro_quantity', models.CharField(max_length=20)),
                ('Order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.ordermodel')),
            ],
        ),
        migrations.CreateModel(
            name='cartmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.productsupload_model')),
            ],
        ),
        migrations.CreateModel(
            name='bookinginfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petname', models.CharField(max_length=30)),
                ('breed', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('petgender', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.registration')),
            ],
        ),
        migrations.AddField(
            model_name='address_details_model',
            name='user_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.registration'),
        ),
        migrations.CreateModel(
            name='wishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groomingapp.productsupload_model')),
            ],
        ),
    ]
