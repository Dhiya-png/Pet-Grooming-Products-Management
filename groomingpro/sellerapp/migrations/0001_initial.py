# Generated by Django 5.0.7 on 2024-07-21 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('cpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
