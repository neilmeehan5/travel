# Generated by Django 5.0.3 on 2024-03-26 17:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl_api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.TextField()),
                ('city', models.TextField()),
                ('activity', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('completed', models.BooleanField(blank=True, default=False)),
                ('recommended', models.BooleanField(blank=True, default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
