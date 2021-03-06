# Generated by Django 3.0.3 on 2020-05-26 16:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_teamname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='belt',
            field=models.CharField(choices=[('White', 'White'), ('White/Yellow', 'White/Yellow'), ('White/Black', 'White/Black'), ('Yellow', 'Yellow'), ('Yellow/Black', 'Yellow/Black'), ('Orange', 'Orange'), ('Orange/Black', 'Orange/Black'), ('Green', 'Green'), ('Green/Black', 'Green/Black'), ('Purple', 'Purple'), ('Purple/Black', 'Purple/Black'), ('Blue', 'Blue'), ('Blue/Black', 'Blue/Black'), ('Brown', 'Brown'), ('Brown/Black', 'Brown/Black'), ('Red', 'Red'), ('Red/Black', 'Red/Black')], default='White', max_length=25),
        ),
        migrations.AddField(
            model_name='profile',
            name='joined',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='RLBW.jpg', upload_to='profile_pics'),
        ),
    ]
