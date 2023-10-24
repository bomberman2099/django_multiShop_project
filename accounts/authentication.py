from django.contrib.auth.backends import BaseBackend
from .models import User


class EmailAuthBackEnd(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Check if username is a valid email address
            if '@' in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(phone=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None