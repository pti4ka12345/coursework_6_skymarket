from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class UserRoles:
    USER = 'user'
    ADMIN = 'admin'
    choices = (
        (USER, _("Пользователь")),
        (ADMIN, _("Администратор"))
    )


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=12, null=True)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=15, choices=(("admin", "admin"), ("user", "user")))
    is_active = models.BooleanField(verbose_name="Аккаунт активен", help_text="Укажите активен ли аккаунт")

    # эта константа определяет поле для логина пользователя
    USERNAME_FIELD = 'email'

    # эта константа содержит список с полями,
    # которые необходимо заполнить при создании пользователя
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    # для корректной работы нам также необходимо
    # переопределить менеджер модели пользователя

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER
