from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from . import models

class UserCreating(UserCreationForm):
    # model = User
    email = forms.CharField(max_length=100)
    class Meta(UserCreationForm.Meta):
        # fields = UserCreationForm.Meta.fields + ('email',)
        fields = ('username', 'password1', 'password2')
    # fields = ('username', 'email', 'password1')

class UserAdditionalInfo(forms.ModelForm):

    class Meta():
        model = models.UserInformation
        fields = ("email", 'email2', "carNumber", "profilePicture")
        labels = {"carNumber": 'Номер вашего автомобиля (по желанию)',
                  "profilePicture": "Аватар",
                  "email2": "Email Confirmation",}

    def clean_email2(self):
        # print("try checks email")
        email1 = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email1 and email2 and email1 != email2:
            print("FIND EMAL ERROR!!")
            raise forms.ValidationError("Email confirmation didn't match.")
        return email2
