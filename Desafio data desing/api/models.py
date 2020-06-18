from django.db import models
from django.core.validators import MinLengthValidator,validate_ipv4_address
from django.core.exceptions import ValidationError

class Agent(models.Model):
    name = models.CharField(("name"), max_length=50)
    status = models.BooleanField(("status"))
    env = models.CharField(("env"), max_length=20)
    version = models.CharField(("version"), max_length=5)
    address = models.CharField(("address"), max_length=39)
    try:
        validate_ipv4_address(address)
    except ValidationError:
        'Invalid IP'
    
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(("name"), max_length=50)
    last_login = models.DateField(("last_login"), auto_now_add=True)
    email = models.EmailField(("email"), max_length=254)
    password = models.CharField(max_length=50, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(("name"), max_length=50)

    def __str__(self):
        return self.name
        
class Event(models.Model):
    LEVELS = (
        ('critical', 'CRITICAL'),
        ('debug', 'DEBUG'),
        ('error', 'ERROR'),
        ('warning', 'WARNING'),
        ('info', 'INFO'),
    )
    level = models.CharField(("level"), max_length=20, choices=LEVELS)
    data = models.TextField(("data"))
    arquivado = models.BooleanField(("arquivado"))
    date = models.DateField(("date"), auto_now_add=True)
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

class GroupUser(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)