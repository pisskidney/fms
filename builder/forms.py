from django import forms
from django.contrib.auth import get_user_model, authenticate
from helpers import get_domain_manager

User = get_user_model()


class SignupForm(forms.Form):
    username = forms.CharField(
        max_length=90,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    email = forms.EmailField(
        max_length=90,
        widget=forms.TextInput(attrs={'placeholder': 'Email'}),
    )
    email_check = forms.EmailField(
        max_length=90,
        widget=forms.TextInput(attrs={'placeholder': 'Confirm email'}),
    )
    password = forms.CharField(
        min_length=8, max_length=90,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    password_check = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),
    )
    error_messages = {
        'invalid_form': ("The user could not be registered because the data "
                         "did not validate."),
        'email_exists': "This email address is already registered.",
        'username_exists': "This username is already registered.",
        'password_mismatch': "Passwords do not match",
        'email_mismatch': "Emails do not match",
    }

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
            raise forms.ValidationError(self.error_messages['username_exists'])
        except User.DoesNotExist:
            pass
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError(self.error_messages['email_exists'])
        except User.DoesNotExist:
            return email

    def clean_email_check(self):
        email1 = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email_check')
        if email1 and email2 and email1 != email2:
            raise forms.ValidationError(
                self.error_messages['email_mismatch']
            )
        return email2

    def clean_password_check(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_check')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch']
            )
        return password1

    def create_user(self, commit=True):
        # call for side effect, populate cleaned_data
        if not self.is_valid():
            raise ValueError(self.error_messages['invalid_form'])
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=90,
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )
    remember = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput,
    )

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if (username and password and user is None):
            raise forms.ValidationError(
                "Please enter a correct username and password"
            )
        return self.cleaned_data

    def get_user(self):
        if not self.is_valid():
            raise ValueError(self.error_messages['invalid_form'])
        return authenticate(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )

    def is_remember(self):
        return self.cleaned_data['remember']


class BuildNameForm(forms.Form):
    name = forms.CharField(
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={'placeholder': 'Website name or keyword'}
        ),
    )

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if 'inhouse' in self.data:
            # Check if the chosen name is indeed free as a subdomain
            pass

        elif 'com' in self.data:
            # Check if the domain is indeed available
            key = name + '.com'
            DomainManager = get_domain_manager()
            dm = DomainManager([key])
            dm.check_domains()
            if not dm.is_valid(key):
                raise forms.ValidationError(
                    'The domain you selected is not available'
                )
        else:
            #@TODO streamline error logging
            raise forms.ValidationError('Unexpected error occured. #0001')
        return self.cleaned_data['name']

    def clean(self):
        return self.cleaned_data


class BuildHomeForm(forms.Form):
    title = forms.CharField(
        required=True,
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Title'}
        ),
    )
    motto = forms.CharField(
        required=False,
        max_length=1024,
        widget=forms.TextInput(
            attrs={'placeholder': 'Motto'}
        ),
    )
    description = forms.CharField(
        required=False,
        max_length=2048,
        widget=forms.TextInput(
            attrs={'placeholder': 'Detailed description'}
        ),
    )
    background = forms.ImageField()

    def clean(self):
        return self.cleaned_data
