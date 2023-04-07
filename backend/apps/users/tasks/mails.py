from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from celery import shared_task
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User


@shared_task
def send_token_email(user_id):
    user = User.objects.get(id=user_id)
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)

    url = f"{settings.BASE_URL}/create-user/?token={str(token)}&id={user.identyfikator}&username={user.username}"
    subject = "Email to login page"
    from_email = settings.EMAIL_HOST_USER
    to = user.email

    text_content = f"""
    Select link below to login\n
    {url}\n
    Remember link expired in 15 minutes
    """

    html_content = f"""
    <h1>Select link below to login</h1>
    <a href="{url}">login link</>
    <p>Remember link expired in 15 minutes</p>
    """
    msg = EmailMultiAlternatives(
        subject,
        text_content,
        from_email,
        [to],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
