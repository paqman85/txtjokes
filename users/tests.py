from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve



class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        reg_user = User.objects.create_user(
            username='Clark',
            email='clarkkent@superman.com',
            password='Iamsuperman123!'
        )
    
        self.assertEqual(reg_user.username, 'Clark')
        self.assertEqual(reg_user.email, 'clarkkent@superman.com')
        self.assertTrue(reg_user.is_active)
        self.assertFalse(reg_user.is_staff)
        self.assertFalse(reg_user.is_superuser)


    def test_create_superuser(self):
        User=get_user_model()
        admin_user = User.objects.create_superuser(
            username='Bruce_Wayne',
            email='brucewayne@waynetech.com',
            password='Batman4life!'
        )

        self.assertEqual(admin_user.username, 'Bruce_Wayne')
        self.assertEqual(admin_user.email, 'brucewayne@waynetech.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response,'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(
            self.response, "Hi There! Want to Have A Bad Time?"
        )
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email
        )
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
