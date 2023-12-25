# Generated by Django 4.2.5 on 2023-12-15 00:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modelrelationshipapp', '0004_alter_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.OneToOneField(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
