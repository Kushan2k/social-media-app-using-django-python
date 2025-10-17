from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailPasswordAuthBackend(ModelBackend):
    """
    Authenticate using email instead of username.
    """
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            return None
        try:
            user = UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
    
    def get_user(self, email):
        try:
            return UserModel.objects.filter(email=email).first()
        except UserModel.DoesNotExist:
            return None
        