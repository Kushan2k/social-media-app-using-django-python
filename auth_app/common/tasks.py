'''
common task will be added here
'''

from django.core.mail import EmailMultiAlternatives
from django.template.loader import  render_to_string
from django.conf import settings

def send_mail_with_template(ctx,subject,email,template_name):
    '''
    sends the mail with the provided template to the provided user
    '''
    try:
        from_email=settings.DEFAULT_EMAIL_USER
        to=email
        html_content=render_to_string(template_name,ctx)

        msg=EmailMultiAlternatives(subject,html_content,from_email,[to])
        msg.attach_alternative(html_content,"text/html")
        msg.send()
    except Exception as e:
        print(f"Error sending email to {email}: {e}")
