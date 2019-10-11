from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users( AbstractUser):
    username =models.CharField(max_length=255)
    email = models.EmailField(
        "email",
        help_text="this field is the loggin username",
        unique= True,
        error_messages = {
            'unique':"a user is invalid"
        }
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username','password' , 'first_name','last_name']

    is_verified = models.BooleanField(default=False)
    
    def __str__ (self):
        return '{} , {} '.format(self.username , self.email)
   