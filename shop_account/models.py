# Core Django imports
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    Permission,
    _user_get_permissions,
)
from django.db.models.signals import post_save

# 3rd-party imports
from django_jalali.db import models as jmodels

# Local imports
from .validators import validate_phone_number


class UserManager(BaseUserManager):
    def create_user(self, email, username, password):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password,
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=177)
    phone_number = models.CharField(
        max_length=11, blank=True, validators=[validate_phone_number]
    )
    first_name = models.CharField(max_length=177, null=True, blank=True)
    last_name = models.CharField(max_length=177, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    permission = models.ManyToManyField(Permission, related_name="users")
    address = models.TextField(blank=True)
    city = models.CharField(max_length=70, blank=True)
    country = models.CharField(max_length=70, blank=True)
    bio = models.TextField(blank=True)
    birthday = models.DateTimeField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    telegram_id = models.CharField(max_length=60, blank=True)
    instagram_id = models.CharField(max_length=60, blank=True)
    website = models.URLField(max_length=255, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ("username",)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    def get_user_permissions(self, obj=None):
        return _user_get_permissions(self, obj, "user")

    def get_all_permissions(self, obj=None):
        return _user_get_permissions(self, obj, "all")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def user_profile_save(sender, **kwargs):
    if kwargs["created"]:
        user_profile = Profile(user=kwargs["instance"])
        user_profile.save()


post_save.connect(user_profile_save, sender=User)
