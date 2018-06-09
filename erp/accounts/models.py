from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserProfileManager(BaseUserManager):
    def create_user(self, name, password):
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, password):
        user = self.create_user(name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def delete_user(self, name):
        user = UserProfile.objects.filter(name=name)
        user.delete()


class UserProfile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=64, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'name'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
