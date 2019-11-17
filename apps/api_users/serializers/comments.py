
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

#serializers
from apps.api_users.serializers import ProfileSerializer ,UsersSerializer

#models
from apps.api_users.models import CommentSkill 
from apps.users.models import Users, Profile ,CV



class CommentsSerializers(serializers.ModelSerializer):
    user_comment=UsersSerializer(read_only=True)
    coments = RecursiveField(many=True , allow_null=True)
    class Meta:
        model = CommentSkill
        fields = '__all__'

    

class CommentsSerializersCreate(serializers.ModelSerializer):
    text = serializers.CharField(max_length=255)
    user_comment=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = CommentSkill
        fields = (
            'user_comment',
            'text'
        )


    def create(self, data ,*args , **kwargs):
        profile =Profile.objects.get(is_cv_porter=True) 
        cv= CV.objects.get(profile=profile)
        comment = CommentSkill.objects.create(**data , cv=cv)
        
        comment.save()
        return comment
        