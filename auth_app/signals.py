from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth import get_user_model



@receiver(post_save,sender=get_user_model())
def create_user_profile(sender,instance,created,**kwargs):
    if created and instance.email:
        print(f'User created: {instance.username}')

        #TODO: send the email verification link to the user
