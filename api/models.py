from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=13, null=True, unique=True,verbose_name="Mobile number")
    photo=models.ImageField(upload_to='profile',verbose_name="Profile photo", null=True, blank=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(str(self.email))
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE,null=True)
    message=models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    def __str__(self):
        return str(self.fromUser.user.email + self.toUser.user.email+  self.fromUser.message)



