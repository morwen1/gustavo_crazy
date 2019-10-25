
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

#serializers
from apps.api_users.serializers import ProfileSerializer

#models
from apps.api_users.models import CommentSkill 
from apps.users.models import Users, Profile ,CV



class CommentsSerializers(serializers.ModelSerializer):
    coments = RecursiveField(many=True , allow_null=True)
    class Meta:
        model = CommentSkill
        fields = '__all__'

    

class CommentsSerializersCreate(serializers.ModelSerializer):
    text = serializers.CharField(max_length=255)
    class Meta:
        model = CommentSkill
        exclude = ('cv','coments','likes',)
    

    def create( data ,*args , **kwargs):
        profile =Profile.objects.get(is_cv_porter=True) 
        cv= CV.objects.get(profile=profile)
        comment = CommentSkill.objects.create(text=data['text'].value, cv=cv)
        comment.save()
        return comment
        