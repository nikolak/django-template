from django.contrib.auth.forms import UserCreationForm

from users.models import Person


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username',)
