# Generated by Django 5.1.3 on 2025-02-03 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appy', '0005_alter_products_options_profile'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
        ),
    ]
