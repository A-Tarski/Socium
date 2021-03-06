# Generated by Django 2.1.4 on 2018-12-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='email2',
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='carNumber',
            field=models.CharField(blank=True, max_length=10, verbose_name='Номер вашего автомобиля (по желанию)'),
        ),
        migrations.AlterField(
            model_name='userinformation',
            name='profilePicture',
            field=models.ImageField(blank=True, upload_to='base/profile_pictures/', verbose_name='Фото профиля'),
        ),
    ]
