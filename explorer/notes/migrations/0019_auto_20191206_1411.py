# Generated by Django 3.0 on 2019-12-06 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0018_auto_20191206_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.FileField(blank=True, help_text='Optional image to add to note.', null=True, upload_to='images/'),
        ),
    ]
