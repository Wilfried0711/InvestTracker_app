from datetime import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
from django.db import models

class CustomUserManager (UserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class User (AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=True, default='', max_length=255, unique=True)
    name = models.CharField(max_length=225, blank=True, default='')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name or self.email.split('@')[0]
    