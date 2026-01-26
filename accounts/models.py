from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.name} - {self.subject}"
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# # Signal to save UserProfile automatically when user is saved
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

# class UserProfile(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # profile_picture = models.ImageField(
#     #     upload_to='profile_pics/',
#     #     blank=True,
#     #     null=True
#     # )

#     # def __str__(self):
#     #     return self.user.username