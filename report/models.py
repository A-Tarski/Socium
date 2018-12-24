from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.utils import timezone
from plate.models import Vehicle_plate

# Create your models here

class Report(models.Model):
    header = models.CharField(max_length=100, verbose_name='Что случилось?', help_text='До 100 символов')
    description = models.TextField(null=True, blank=True,verbose_name='Расскажите подробнее (Необязательно)')
    video_link_report = models.URLField(null=True, blank=True, verbose_name='Ссылка на видео', help_text='YouTube')
    image_report = models.ImageField(upload_to='report/images/', null=True, blank=True, verbose_name='Загрузите Ваше Фото', help_text='На фото должно быть видно номер автомобиля!')
    created_date = models.DateTimeField(auto_now_add=True) #auto_now_add=True,
    last_modified = models.DateTimeField(auto_now=True) #auto_now=True,
    vehicle_plate = models.ForeignKey(Vehicle_plate, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_date']

    def get_absolute_url(self):
        return reverse('report:detail', kwargs={'pk':self.pk})

    def get_likes(self):
        return Like.objects.filter(report=self, side=True).count()

    def get_unlikes(self):
        return Like.objects.filter(report=self, side=False).count()

    def __str__(self):
        return self.header

class Like(models.Model):
    side = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='likes')
    add_date = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    body = models.TextField()
    report = models.ForeignKey(Report, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now=True)
