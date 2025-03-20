from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from .models import Post

# Create your tests here.
class BlogTestClass(TestCase):
    def setUp(self):
        """ Set up test user and test post """
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.post = Post.objects.create(
            title='test Post',
            text='This is a test post',
            author = self.user,
            published_date = timezone.now()
        )

    def test_post_list_view(self):
        """ Test if the post list view loads correctly and displays posts """
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, 'test Post') # Check if post is displayed

    def test_post_detail_view(self):
        """ Test if the post detail view loads correctly and displays a specific post """
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
        self.assertContains(response,'This is a test post')


