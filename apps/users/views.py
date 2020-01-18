from django.conf import settings
from django.http import JsonResponse
from django.views.generic import CreateView

from apps.users.models import User
from django import forms


def get_public_key(request):
    return JsonResponse(settings.JWT_PUBLIC_KEY)


class CreateUserForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data.get("confirm_password") != self.cleaned_data.get(
            "password"
        ):
            raise forms.ValidationError("Senhas não são iguais")

    def clean_password(self):
        if self.cleaned_data.get("confirm_password") != self.cleaned_data.get(
            "password"
        ):
            raise forms.ValidationError("Senhas não são iguais")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password", "confirm_password"]


class UserCreateView(CreateView):
    model = User
    template_name = "registration/registration.html"
    form_class = CreateUserForm
    # fields = ["first_name", "last_name"s, "email", "password", "confirm_password"]
