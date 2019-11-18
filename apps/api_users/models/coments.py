from django.db import models
from apps.users.models import Users



class CommentSkill(models.Model):
    """
        comments of anything is a test for skills

    """
    cv= models.ForeignKey(to='users.CV' , on_delete=True)
    user_comment = models.ForeignKey(to=Users , on_delete=False)
    coments = models.ManyToManyField(
        to='api_users.CommentSkill' , 
                
        blank=True
        )
    
    text = models.TextField()
    reply = models.BooleanField(default=False)
    
    


    def __str__(self):
        return 'comment  to cv {}'.format( self.cv)

    

class CommentsLikes(models.Model):
    user = models.ForeignKey(to=Users, on_delete=False )
    comment=models.ForeignKey(to=CommentSkill,related_name='comment_likes', on_delete=models.CASCADE)
