import re
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import ValidationError
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

User = get_user_model()

def authenticate_user(identifier, password):
    user = User.objects.filter(email=identifier).first() or User.objects.filter(username=identifier).first()
    
    if not user:
        raise ValidationError({"error": "Invalid username/email or password."})

    if not user.check_password(password):
        raise ValidationError({"error": "Invalid username/email or password."})

    if not user.is_active:
        raise ValidationError({"error": "This account is inactive."})

    refresh = RefreshToken.for_user(user)

    return {
        "access_token": str(refresh.access_token),
        "refresh_token": str(refresh)
    }


def reset_password(uidb64, token, new_password):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        raise ValidationError({"error": "Invalid link."})

    if not default_token_generator.check_token(user, token):
        raise ValidationError({"error": "Invalid or expired link."})

    if len(new_password) < 8:
        raise ValidationError({"error": "Password must be at least 8 characters long."})

    if not re.search(r'[A-Z]', new_password):
        raise ValidationError({"error": "Password must contain at least one uppercase letter."})

    if not re.search(r'[0-9]', new_password):
        raise ValidationError({"error": "Password must contain at least one digit."})

    user.set_password(new_password)
    user.save()
    
    return {"message": "Your password has been successfully reset."}