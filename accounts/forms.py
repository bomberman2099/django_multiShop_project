from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core import validators
from django.core.exceptions import ValidationError
from accounts.models import User


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="گذرواژه", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="تکرار گذرواژه", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["email", "fullname"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ["email", "password", "fullname", "is_active", "is_admin"]

def start_with_0(value):
    if value[0]!='0':
        raise forms.ValidationError("شماره تلفن بایستی با 0 شروع شود")

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your phone number', })
        , validators=[]
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Your password'}),
    )

    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if len(phone) > 12:
    #         raise ValidationError(
    #             'invalid value: %(value)s is invalid',
    #             code='invalid',
    #             params={'value': f'{phone}'},
    #         )
    # def clean(self):
    #     cd = super().clean()
    #     phone = cd.get('phone') # or cd['phone']
    #     #     if len(phone) > 12:
    #     #         raise ValidationError(
    #     #             'invalid value: %(value)s is invalid',
    #     #             code='invalid',
    #     #             params={'value': f'{phone}'},
    #     #         )


class RegisterForm(forms.Form):
    phone = forms.CharField(label='username',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your phone number'})
        , validators=[validators.MaxLengthValidator(11), start_with_0]
    )


class CheckOTPForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Your phone number', })
        , validators=[validators.MaxLengthValidator(4)]
    )
