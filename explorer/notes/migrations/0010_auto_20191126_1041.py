# Generated by Django 2.2.5 on 2019-11-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0009_auto_20191125_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.ImageField(blank=True, help_text='Optional image to add to note.', upload_to='media'),
        ),
    ]