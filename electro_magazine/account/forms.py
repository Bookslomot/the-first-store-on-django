from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import request

from account.models import User
from cart.models import Customer


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput)

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, help_text='Пароль не должен быть распространенным и так же ОБЯЗАН иметь больше 8 символов')

    confirm_password = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)

    email = forms.EmailField(label='Электронная почта')

    phone = forms.CharField(label='Номер телефона')


    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'email', ]

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Адрес {email} уже занят, ввыберите другой'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Имя {username} занято, попробуйте выбрать другое имя'
            )
        return username

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError(
                f'Пароли не совпадают, в поле пароля учитывается регистр'
            )
        return self.cleaned_data


class UpdateProfileUserForm(forms.ModelForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput)

    email = forms.CharField(label='Почта', widget=forms.TextInput)

    phone = forms.CharField(label='Номер телефона', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Адрес {email} уже занять выберите другой'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Имя {username} занято, попробуйте выбрать другое имя'
            )
        return username







