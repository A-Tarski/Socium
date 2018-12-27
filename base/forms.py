from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models
import re

class UserCreating(UserCreationForm):

    username = forms.CharField(max_length=10, label='Имя пользователя', help_text='Не более 10 символов')

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if len(re.findall('[^A-Za-z0-9_]', username)):
            raise forms.ValidationError("Имя пользователя содержит недопустимые символы")
        return username


    class Meta():
        model = User
        fields = ('username', 'password1', 'password2')

class UserAdditionalInfo(forms.ModelForm):

    class Meta():
        model = models.UserInformation
        fields = ("email", 'email2', "carNumber", "profilePicture")

    def clean_email2(self):
        email1 = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email1 and email2 and email1 != email2:
            print("FIND EMAL ERROR!!")
            raise forms.ValidationError("Email confirmation didn't match.")
        return email2

class UserUpdateForm(forms.ModelForm):

    class Meta():
        model = models.UserInformation
        fields = ("profilePicture", "carNumber")
