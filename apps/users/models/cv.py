from django.db import models 

class Skills (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pt = models.IntegerField()
    def __str__(self):
        return self.name


class Experiences (models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return self.name

class PersonalRef(models.Model):
    person_ref_name = models.CharField(max_length=200 , unique=True)
    person_ref_email = models.EmailField(max_length=200)
    person_ref_title_prof = models.CharField(max_length=200)
    def __str__(self):
        return self.person_ref_name

class CV(models.Model):
    profile = models.ForeignKey(to = 'users.Profile' , on_delete=None)
    skills = models.ManyToManyField(to=Skills)
    experiences = models.ManyToManyField(to=Experiences)
    personal_ref = models.ManyToManyField(to=PersonalRef )
    def __str__(self):
        return 'cv of '.format(self.profile.user.email)
