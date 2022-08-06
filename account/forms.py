from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Assassin, User, SUBJECT_CHOICES, COLLEGE_CHOICES
from django import forms

# RegisterUserForm
# UpdateUserForm

# CreateAssassinForm
# UpdateAssassinForm

# PayMembershipForm - placeholder sets up a flag, todo improve

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {
            'username': None,
        }

class UpdateUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': None,
        }

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
        self.fields['new_password2'].label = "New password"

class CreateAssassinForm(forms.ModelForm):
    class Meta:
        model = Assassin
        fields = ['pseudonym', 'discordName', 'discordTag', 'subject', 'college', 'startYear', 'address', 'room', 'postal']

    def clean_discordTag(self):
        data = self.cleaned_data['discordTag']
        if data < 0 or data > 9999:
            raise forms.ValidationError("Invalid Discord Tag!")
        return data
    
class UpdateAssassinForm(forms.ModelForm):
    class Meta:
        model = Assassin
        fields = ['pseudonym', 'discordName', 'discordTag', 'subject', 'college', 'startYear', 'address', 'room', 'postal']

    def clean_discordTag(self):
        data = self.cleaned_data['discordTag']
        if data < 0 or data > 9999:
            raise forms.ValidationError("Invalid Discord Tag!")
        return data

class PayMembershipForm(forms.Form):
    pass