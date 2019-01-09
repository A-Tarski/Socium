from django.db import models
from django.contrib.auth.models import User
from report.models import Comment, Report, Like
from django.urls import reverse, reverse_lazy
# Create your models here.

class UserInformation(models.Model):
    carNumber = models.CharField(max_length=10, blank=True, verbose_name='Номер вашего автомобиля (по желанию)')
    profilePicture = models.ImageField(upload_to='base/profile_pictures/', blank=True, verbose_name='Фото профиля')
    email = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return self.user.username

    def find_comments(self):
        return Comment.objects.filter(user=self.user).count()

    def find_reports(self):
        return Report.objects.filter(user=self.user).count()

    def find_likes(self):
        return Like.objects.filter(user=self.user).count()

    def get_absolute_url(self):
        return reverse_lazy('base:personal', kwargs={"username": self.user.username})
