from django.db.models.signals import pre_delete
from django.dispatch import receiver
from . coments import * 

@receiver(pre_delete ,sender=CommentSkill , dispatch_uid="deleting_all_commentslikes" )
def delete_comments_likes(sender , **kwargs):
    comment= kwargs['instance']
    if comment.pk :
        comment.coments.all().delete()
        CommentsLikes.objects.filter(comment=comment.pk).delete()
    