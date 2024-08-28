from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, mobile, pin, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, mobile=mobile, **extra_fields)
        user.set_password(pin)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, mobile, pin, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, mobile, pin, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    pin = models.CharField(max_length=3, validators=[MinLengthValidator(3), MaxLengthValidator(4)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile', 'pin']

    def __str__(self):
        return self.email

class BlogPost(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    heading = models.CharField(max_length=150)
    summary = models.TextField(max_length=400, blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-timestamp']
