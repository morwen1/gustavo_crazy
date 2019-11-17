from django.db import models
from apps.users.models import Users



"""
comments of anything is a test for skills

"""

class CommentSkill(models.Model):
    cv= models.ForeignKey(to='users.CV' , on_delete=True)
    user_comment = models.ForeignKey(to=Users , on_delete=False)
    coments = models.ManyToManyField(to='api_users.CommentSkill' , blank=True)
    likes =models.IntegerField(default=0)
    text = models.TextField()
    reply = models.BooleanField(default=False)
    def __str__(self):
        return 'comment  to cv {}'.format( self.cv)
