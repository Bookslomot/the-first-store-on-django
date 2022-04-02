from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('User must have a username')
        if email is None:
            raise TypeError('User must have a email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Superuser must have a password')

        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=255, db_index=True, verbose_name='Имя пользователя', unique=True)

    email = models.EmailField(max_length=255, db_index=True, unique=True, verbose_name='Почта')

    status = models.CharField(verbose_name='Пользовательский статус', max_length=255, null=True, blank=True,
                              help_text='Статус, кторый может ввести пользователь, например: "У меня сегодня отличное настроение"')

    is_active = models.BooleanField(default=True, verbose_name='Состояние профиля пользвателя')

    is_staff = models.BooleanField(default=False, verbose_name='Права администрации')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')

    photo = models.ImageField(upload_to='photo/%Y/%m/%d', null=True, blank=True, verbose_name='Фото пользователя')

    phone = models.CharField(verbose_name='Номер телефона', max_length=20, null=True, blank=True, default=None)

    address = models.CharField(verbose_name='Адрес', max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'Пользователь - {self.email} ({self.username})'

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username




