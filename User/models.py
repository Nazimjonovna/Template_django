from django.db import models

# Create your models here.
class UserData(models.Model):
    email = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    otp = models.CharField(max_length=255, null=True)
    parol = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to='acc/', null=True, blank=True)
    bio = models.CharField(max_length=255, null=True)
    link = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username


class PostData(models.Model):
    user = models.ForeignKey(UserData, on_delete=models.CASCADE)
    file = models.FileField(upload_to = 'post/')
    comment = models.CharField(max_length=255, null=True)
    like = models.IntegerField()


