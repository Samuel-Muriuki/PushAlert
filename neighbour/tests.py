from django.test import TestCase
from .models import Post, neighbourhood
# Create your tests here.
class neighbourhoodTestClass(TestCase):
    def setUp(self):
        self.Centum = neighbourhood(neighbourhood='Centum')

    def test_instance(self):
        self.assertTrue(isinstance(self.Centum,neighbourhood))

    def tearDown(self):
        neighbourhood.objects.all().delete()

    def test_save_method(self):
        self.Centum.save_neighbourhood()
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)>0)

    def test_delete_method(self):
        self.Centum.delete_neighbourhood('Centum')
        hood = neighbourhood.objects.all()
        self.assertTrue(len(hood)==0)

class PostTestClass(TestCase):
    def setUp(self):
        self.Hurlingham = Post(Hurlingham='Hurlingham')

    def test_instance(self):
        self.assertTrue(isinstance(self.Hurlingham))

    def tearDown(self):
        Post.objects.all().delete()

    def test_save_method(self):
        self.Hurlingham.save_Hurlingham()
        rest = Post.objects.all()
        self.assertTrue(len(rest)>0)

    def test_delete_method(self):
        self.Hurlingham.delete_Hurlingham('Hurlingham')
        rest = Post.objects.all()
        self.assertTrue(len(rest)==0)