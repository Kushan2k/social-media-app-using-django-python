from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .common.tasks import send_mail_with_template
from django.utils.timezone import now



@receiver(post_save,sender=get_user_model())
def create_user_profile(sender,instance,created,**kwargs):
    if created and instance.email:
        print(f'User created: {instance.username}')

        context = {
            "user": instance,
            "username": getattr(instance, "username", ""),
            "code": instance.verification_code,
            "verification_url": "",
            "expires_in_minutes": 15,
            "year": now().year,
        }

        send_mail_with_template(context,"Verify your email",instance.email, "email/register_email.html")
