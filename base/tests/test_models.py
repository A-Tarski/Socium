from django.test import TestCase
from base.models import UserInformation
from django.contrib.auth.models import User


# class UserInformation(models.Model):
#     carNumber = models.CharField(max_length=10, blank=True, verbose_name='Номер вашего автомобиля (по желанию)')
#     profilePicture = models.ImageField(upload_to='base/profile_pictures/', blank=True, verbose_name='Фото профиля')
#     email = models.EmailField()
#     # ???????????!!!!!!!!!!!!!WHY IT'S HERE???!?!?!?!?!
#     email2 = models.EmailField(verbose_name='Подтверждение Email', help_text='Для подтверждения введите, пожалуйста, Ваш Email ещё раз.')
#     user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True)
#
#     def __str__(self):
#         return self.user.username
#
#     def find_comments(self):
#         return Comment.objects.filter(user=self.user).count()
#
#     def find_reports(self):
#         return Report.objects.filter(user=self.user).count()
#
#     def find_likes(self):
#         return Like.objects.filter(user=self.user).count()
#
#     def get_absolute_url(self):
#         return reverse_lazy('base:personal', kwargs={"username": self.user.username})

class UserInformationModelTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="User1", email='user1@gmail.com')
        UserInformation.objects.create(carNumber="a100аа777", user=User.objects.get(id=1))

    def setUp(self):
        pass

    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)
    #
    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    def test_carNumber_verbose_name(self):
        user_info = UserInformation.objects.get(id=1)
        verbose_name = user_info._meta.get_field("carNumber").verbose_name
        self.assertEqual(verbose_name, 'Номер вашего автомобиля (по желанию)')

    def test_carNumber_can_be_blank(self):
        user_info = UserInformation.objects.get(id=1)
        self.assertTrue(user_info._meta.get_field("carNumber").blank)

    def test_carNumber_max_length(self):
        user_info = UserInformation.objects.get(id=1)
        max_length = user_info._meta.get_field("carNumber").max_length
        self.assertEqual(max_length, 10)

    def test_profile_picture_upload_directory(self):
        user_info = UserInformation.objects.get(id=1)
        upload_dir = user_info._meta.get_field("profilePicture").upload_to
        self.assertEqual(upload_dir, "base/profile_pictures/")

    def test_user_to_userinfo_one_to_one_linking(self):
        user_info = UserInformation.objects.get(id=1)
        user = User.objects.get(id=1)
        self.assertEqual(user, user_info.user)

    def test_userinfo_cascade_deleting(self):
        user = User.objects.get(id=1)
        user.delete()
        with self.assertRaises(UserInformation.DoesNotExist):
            user_info = UserInformation.objects.get(id=1)

    def test_userinfo_absolute_url(self):
        user_info = UserInformation.objects.get(id=1)
        # print(user_info.get_absolute_url())
        self.assertEqual(user_info.get_absolute_url(), "/personal/User1")
