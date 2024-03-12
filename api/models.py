from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin,BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_superuser(self, email,password=None,**extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
class User(AbstractUser,PermissionsMixin):
    username = models.CharField(
        max_length=50, blank=False, null=True,verbose_name="user name")
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(max_length=13, null=True, unique=True,verbose_name="Mobile number")
    photo=models.ImageField(upload_to='profile',verbose_name="Profile photo", null=True, blank=True)
    is_verified=models.BooleanField(default=False)
    online_status=models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS = ["username"]
    # objects = UserManager()
    def __str__(self):
        return "{}".format(str(self.email))
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE,null=True)
    message=models.TextField(null=True, blank=True)
    thread_name=models.CharField(max_length=50,null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    
    def __str__(self):
        return str(self.fromUser.user.email + self.toUser.user.email+  self.fromUser.message)



