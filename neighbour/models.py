from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from phone_field import PhoneField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name="hood", null=True)
    hood_logo = CloudinaryField('image')
    description = models.TextField()
    health_tell = PhoneField(null=True, blank=True)
    police_number = PhoneField(null=True, blank=True)
    area_administrator = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    def update_neighborhood(self):
        self.update()

    def update_occupants(self):
        self.update()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=400, blank=True)
    name = models.CharField(blank=True, max_length=120)
    profile_pic = CloudinaryField('image', default='https://res.cloudinary.com/samm-gallery/image/upload/v1649751098/Ninja_fjh4xm.png')
    phone_number = PhoneField(max_length=15, blank=True)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
