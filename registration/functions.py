from django.contrib.auth.models import User

def check_email(email):
    users=User.objects.filter(email=email)
    if users.exists():
        return False
    else:
        return True