from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'organization']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Structure(models.Model):
    LOCATION_CHOICES = [
        ('ALP', 'Alappuzha'),
        ('EKM', 'Ernakulam'),
        ('KKD', 'Kozhikode'),
        ('PLK', 'Palakkad'),
        ('KLM', 'Kollam'),
        ('KNR', 'Kannur'),
        ('KSD', 'Kasargod'),
        ('IDK', 'Idukki'),
        ('KTM', 'Kottayam'),
        ('TSR', 'Thrissur'),
        ('PTA', 'Pathanamthitta'),
        ('MLP', 'Malappuram'),
        ('WYD', 'Wayanad'),
        ('TVM', 'Thiruvananthapuram'),
    ]

    STRUCTURE_CHOICES = [
        ('BR', 'Bridge'),
        ('BL', 'Building'),
        ('DM', 'Dam'),
        ('SL', 'Slope'),
        ('TW', 'Tower'),
        ('OT', 'Other'),
    ]

    name = models.CharField(max_length=255, help_text="Name of Your Structure")
    location = models.CharField(max_length=3, choices=LOCATION_CHOICES, help_text="Location of Your Structure")
    structure_type = models.CharField(max_length=2, choices=STRUCTURE_CHOICES, help_text="Type of Structure")
    images = models.ImageField(upload_to='structure_images/', blank=True, null=True)

    def __str__(self):
        return self.name