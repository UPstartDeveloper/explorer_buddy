# Generated by Django 2.2.7 on 2019-11-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='media',
            field=models.ImageField(help_text='Optional image to add to note.', upload_to='media'),
        ),
    ]
