from django.test import TestCase
from base.views import UserUpdateView
from base.models import UserInformation
from django.contrib.auth.models import User
from django.urls import reverse
from base import forms



class UserUpdateViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass
        User.objects.create(username='test', password='vierhfe')
        UserInformation.objects.create(carNumber="a100аа777", user=User.objects.get(id=1))

    def test_update_view_existance(self):
        resp = self.client.get(reverse('base:edit', kwargs={'slug':'test'}))
        self.assertTemplateUsed(resp, 'base/userinformation_form.html')

    def test_create_new_user_right_template(self):
        resp = self.client.get(reverse('base:sign_up'))
        self.assertTemplateUsed(resp, 'registration/sign_up.html')

    def test_create_new_user_right_context(self):
        resp = self.client.get(reverse('base:sign_up'))
        self.assertIn('userAdditionalForm', resp.context)
        self.assertIn('userCreateForm', resp.context)

    def test_create_new_user_post(self):
        form_data = {'email': "test5@gmail.com", 'email2':'test5@gmail.com'}
        info_form = forms.UserAdditionalInfo(data=form_data)
        form_data = {'username': "test5", 'password1':'wjkcjbwc', 'password2':'wjkcjbwc'}
        user_form = forms.UserCreating(data=form_data)
        resp = self.client.post(reverse('base:sign_up'), {'userAdditionalForm': info_form,
                                                                 'userCreateForm': user_form,})
        print(resp.status_code)
        user = User.objects.get(username="test5")
        user_link = UserInformation.objects.get(email="test5@gmail.com").user
        self.assertEqual(user, user_link)
