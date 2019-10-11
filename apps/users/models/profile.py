from django.db import models



class Profile ( models.Model ):
    user = models.OneToOneField(to ='users.Users' ,on_delete=models.CASCADE, unique=True)
    age = models.SmallIntegerField()
    addres = models.TextField()
    is_admin = models.BooleanField(default=False)
    is_cv_porter = models.BooleanField(default=False)
    cellphone = models.CharField(max_length=10)
    linkedin = models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    
    def __str__(self):
        return 'profile of {}'.format(self.user.email)