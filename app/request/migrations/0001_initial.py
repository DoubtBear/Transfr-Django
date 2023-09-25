# Generated by Django 3.1.7 on 2021-04-02 05:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riderLocation', models.TextField()),
                ('destination', models.TextField()),
                ('date', models.DateTimeField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('rider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
