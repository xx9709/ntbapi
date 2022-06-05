
from django.db import models
from django.contrib.auth.models import AbstractUser
from complex import Complex

class UserRoleChoice(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    MASTER = 'master', 'Master'
    PRORAB = 'prorab', 'Prorab'
    UCHASNIK = 'uchasni', 'Uchasnik'
    DIRECTOR = 'director', 'Director'
    BUGALTER = 'bugalter', 'Bugalter'
    PTO = 'pto', 'Pto'
    TASISCHI = 'tasischi', 'Tasischi'
    TAMINOTCHI = 'taminotchi', 'Taminotchi'
    SKLADCHI = 'skladchi', 'Skladchi'
    BRIGADIR = 'brigadir', 'Brigadir'


class User(AbstractUser):
    user_role = models.CharField(max_length=50, choices=UserRoleChoice.choices, default=UserRoleChoice.MASTER)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    usernames = None
    bill = models.IntegerField(default=0)
    workplace = models.ForeignKey(Complex, null = True, blank=True, on_delete=models.SET_NULL)

    USERNAMEE_FIELD = 'email'
    REQUIRED_FILELDS = ['user_role']