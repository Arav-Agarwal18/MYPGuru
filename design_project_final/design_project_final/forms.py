from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your forms here.

class Login(UserCreationForm):
    username = forms.CharField(required=True, min_length=8)
    
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
    
    def save(self, commit=True):
        user = super(Login, self)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user