from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username",)


class UserUpdateForm(forms.ModelForm):

    username = forms.CharField(disabled=True)

    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "gender", "phone")
        labels = {
            "first_name": _("Prénom"),
            "last_name": _("Nom de famille"),
        }
