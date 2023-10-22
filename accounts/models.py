from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .usermanager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )
    fullname = models.CharField(max_length=50, verbose_name="نام کامل")
    phone = models.CharField(max_length=12,unique=True, verbose_name='شماره تلفن')
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = ['fullname', 'email']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return f"{self.phone} - {self.fullname}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



class OTP(models.Model):
    token = models.CharField(max_length=90, null=True)
    phone = models.CharField(max_length=11)
    code = models.CharField(max_length=4)
    expiration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone