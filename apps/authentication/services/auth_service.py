from enum import Enum
from django.contrib.auth import authenticate, login


class EventAuth(Enum):
    LOGIN = None
    REGISTER = None


def get_user(event_auth, form):
    if event_auth.LOGIN:
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        return user
    if event_auth.REGISTER:
        first_name = form.cleaned_data.get("first_name")
        last_name = form.cleaned_data.get("last_name")
        email = form.cleaned_data.get("email")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(first_name=first_name, last_name=last_name, email=email, password=raw_password)
        return user
