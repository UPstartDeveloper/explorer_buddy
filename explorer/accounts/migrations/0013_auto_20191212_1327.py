# Generated by Django 3.0 on 2019-12-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20191212_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mugshot',
            field=models.ImageField(blank=True, default='images/user-icon.png', help_text='User profile image', upload_to='images/'),
        ),
    ]
