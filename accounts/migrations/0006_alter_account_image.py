# Generated by Django 4.1.1 on 2023-03-14 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_account_identification_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='users'),
        ),
    ]