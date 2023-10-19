from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from .usermanager import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="آدرس ایمیل",
        max_length=255,
        unique=True,
    )
    fullname = models.CharField(max_length=50, verbose_name="نام کامل")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربر ها'

    def __str__(self):
        return self.email

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

