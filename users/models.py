from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Поле Email должно быть заполнено")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_active', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Пользователь должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Пользователь должен иметь is_superuser=True")
        return self.create_user(email=email, password=password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Логин'
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Электронная почта",
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Фамилия",
    )
    is_organizer = models.BooleanField(
        default=False,
        verbose_name="Организатор"
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name="Суперпользователь"
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ['-updated_at']

    def __str__(self):
        return self.email
