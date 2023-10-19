from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,email, phone, fullname, password=None):
        """
        Creates and saves a User with the given phone, date of
        birth and password.
        """
        if not phone:
            raise ValueError("Users must have an phone")

        user = self.model(
            phone=phone,
            email=self.normalize_email(email),
            fullname=fullname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email, phone, fullname, password=None):
        """
        Creates and saves a superuser with the given phone, date of
        birth and password.
        """
        user = self.create_user(
            email= email,
            phone= phone,
            password=password,
            fullname=fullname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
