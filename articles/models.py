from django.db import models
from django.contrib.auth.models import User
## importing post_save and reciever for updating profile
from django.db.models.signals import post_save
from django.dispatch import receiver



# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     description = models.CharField(max_length=100, default='')
#     city = models.CharField(max_length=100, default='')
#     website = models.URLField(default='')
#     phone = models.IntegerField(default=0)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50, default='')
    # first_name = models.CharField(max_length=50, default='')
    # last_name = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    # email = models.ForeignKey(max_length=200, default='')
    # image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.username

## for updating profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

## for saving update hook >>> profile
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Articles(models.Model):
    title = models.CharField(max_length=100, )
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]
