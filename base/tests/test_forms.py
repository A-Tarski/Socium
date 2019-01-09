from django.test import TestCase
from base.forms import UserCreating, UserAdditionalInfo

# class UserCreating(UserCreationForm):
#
#     username = forms.CharField(max_length=10, label='Имя пользователя', help_text='Не более 10 символов')
#
#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if len(re.findall('[^A-Za-z0-9_]', username)):
#             raise forms.ValidationError("Имя пользователя содержит недопустимые символы")
#         return username
#
#     class Meta():
#         model = User
#         fields = ('username', 'password1', 'password2')
#
# class UserAdditionalInfo(forms.ModelForm):
#
#     email2 = forms.EmailField(label='Подтверждение Email', help_text='Для подтверждения введите, пожалуйста, Ваш Email ещё раз.')
#
#     class Meta():
#         model = models.UserInformation
#         fields = ("email", 'email2', "carNumber", "profilePicture")
#
#     def clean_email2(self):
#         email1 = self.cleaned_data.get("email")
#         email2 = self.cleaned_data.get("email2")
#         if email1 and email2 and email1 != email2:
#             print("FIND EMAL ERROR!!")
#             raise forms.ValidationError("Вы ввели разные Email адреса")
#         return email2
#
# class UserUpdateForm(forms.ModelForm):
#
#     class Meta():
#         model = models.UserInformation
#         fields = ("profilePicture", "carNumber")


class UserCreatingFormTestClass(TestCase):

    def test_user_creating_form_username_max_length(self):
        form_data = {'username': "0123456789_", 'password1':'wjkcjbwc', 'password2':'wjkcjbwc'}
        form = UserCreating(data=form_data)
        self.assertFalse(form.is_valid())

    def test_user_creating_form_username_not_allowed_symbols(self):
        for symbol in "!@#$%^&*()+§±';:фй¡™£¢∞§¶•ªº–≠":
            form_data = {'username': "test" + symbol, 'password1':'wjkcjbwc', 'password2':'wjkcjbwc'}
            # print(form_data)
            form = UserCreating(data=form_data)
            self.assertFalse(form.is_valid())

class UserAdditionslInfoFormTestClass(TestCase):

    def test_email1_and_email2_identical(self):
        form_data = {'email': "test@gmail.com", 'email2':'test1@gmail.com'}
        form = UserAdditionalInfo(data=form_data)
        self.assertFalse(form.is_valid())

    def test_email1_and_email2_is_blank(self):
        form_data = {'email': "", 'email2':""}
        form = UserAdditionalInfo(data=form_data)
        self.assertFalse(form.is_valid())
