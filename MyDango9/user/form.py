from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = UserCreationForm.Meta.fields + ('email','mobile','weChat','qq')