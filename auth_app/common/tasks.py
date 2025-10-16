from django.core.mail import EmailMultiAlternatives
from django.template.loader import  get_template,render_to_string
from django.conf import settings




async def send_mail_with_template(email,token):
    subject="Activate your account"
    from_email=settings.EMAIL_HOST_USER
    to=email

    text_content=render_to_string('email/activation.txt',{'token':token})
    html_content=render_to_string('email/activation.html',{'token':token})

    msg=EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()