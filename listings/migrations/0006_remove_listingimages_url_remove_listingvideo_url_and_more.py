# Generated by Django 4.1.1 on 2022-12-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('listings', '0005_rename_name_listing_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingimages',
            name='url',
        ),
        migrations.RemoveField(
            model_name='listingvideo',
            name='url',
        ),
        migrations.AddField(
            model_name='listingimages',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='uploader.dropbox'),
        ),
        migrations.AddField(
            model_name='listingvideo',
            name='video',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='uploader.dropbox'),
        ),
        migrations.AlterField(
            model_name='listingfloorplan',
            name='floor_plan',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='uploader.dropbox'),
        ),
    ]