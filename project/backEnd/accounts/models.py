from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField
from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(db_index=True, unique=True)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
    
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    