# Generated by Django 2.2.5 on 2019-11-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0010_auto_20191126_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.ImageField(blank=True, help_text='Optional image to add to note.', upload_to=b'media'),
        ),
    ]