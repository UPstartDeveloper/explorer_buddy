# Generated by Django 3.0 on 2019-12-12 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notes', '0020_auto_20191206_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='author',
            field=models.ForeignKey(help_text='The explorer making this log.', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]