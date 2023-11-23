from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models.fields import BooleanField
from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(db_index=True, unique=True)
    
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)    
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False) 
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = [
    
    ]
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    