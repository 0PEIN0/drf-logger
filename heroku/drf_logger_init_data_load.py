from django.conf import settings
from django.contrib.auth.models import User

super_user_email_list = [settings.ADMIN_USER_EMAIL]
super_user_password_list = [settings.ADMIN_USER_PASSWORD]


def create_super_user(email, password):
    if User.objects.filter(email=email).count() is 0:
        user = User.objects.create_superuser(
            username=email, email=email, password=password)
    else:
        user = User.objects.get(email=email)
    return user

# Create super users
super_user_list = []
for i in range(len(super_user_email_list)):
    super_user_list.append(create_super_user(
        email=super_user_email_list[i], password=super_user_password_list[i]))
