from django.core.mail import EmailMessage

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.urls import reverse


def send_email_confirmation(user, request):
    token = default_token_generator.make_token(user)
    uid = user.pk
    confirmation_link = request.build_absolute_uri(
        reverse('users:confirm-email', kwargs={'uid': uid, 'token': token})
    )
    subject = "Confirm Your Email Address"
    message = render_to_string('auth/email_confirmation.html', {
        'user': user,
        'confirmation_link': confirmation_link,
    })

    email = EmailMessage(subject,
                         message,
                         settings.EMAIL_HOST_USER,
                         [user.email])
    email.content_subtype = 'html'
    email.send()
