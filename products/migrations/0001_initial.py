# Generated by Django 3.0.7 on 2020-07-23 13:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2020, 7, 23, 19, 32, 11, 444453))),
                ('body', models.TextField()),
                ('url', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
                ('icon', models.ImageField(upload_to='images/')),
                ('votes_total', models.IntegerField(default=1)),
                ('hunter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
