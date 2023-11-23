from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    # All user
    def create_user(self, email, password, **extra_fields):
    
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # admin user
    def create_superuser(self, email, password, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)
        # extra_fields.setdefault('is_active', True)

        if password is None:
            raise TypeError('Superuser must have a password.')
        
        # "create_user"함수를 이용해 우선 사용자를 DB에 저장
        user = self.create_user(email, password, **extra_fields)

        # 관리자로 지정
        # user.is_superuser = True
        # user.is_staff = True
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True   
        user.save()
        
        return user
        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError(_('Superuser must have is_staff=True.'))
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError(_('Superuser must have is_superuser=True.'))
        # return self.create_user(email, password, **extra_fields)