# Generated by Django 2.1.4 on 2018-12-20 16:04

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
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carNumber', models.CharField(blank=True, max_length=10)),
                ('profilePicture', models.ImageField(blank=True, upload_to='base/profile_pictures/')),
                ('email', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
