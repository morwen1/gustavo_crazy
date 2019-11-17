from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.users.models import Profile
from .users import UsersSerializer

class ProfileSerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
    linkedin = serializers.URLField()
    github = serializers.URLField()
    class Meta:
        model =Profile
        fields = (
            'id',
            'user',
            'age',
            'addres',
            'linkedin',
            'github',
            )
    def validate_addres(self ,data):
        addres = data
        #import pdb; pdb.set_trace()
        if type(addres) != str : 
            raise serializers.ValidationError('type of addres is string')
        elif len(addres) < 10 :
            raise serializers.ValidationError('the address is to short')

        try :
            int(addres)
            raise serializers.ValidationError('type of addres is string')

        except:
            return addres
    

    def validate_age(self, data):
        age = data
        if type(age) != int :
            raise serializers.ValidationError('age minors not admited')
        if age < 18:
            raise serializers.ValidationError('age is minor of 18')
        return age
"""
def ProfileSerializerCreate(ModelSerializer):
    user= serializers.HiddenField(serializers.CurrentUserDefault())
    class Meta:
        model=Profile
        fields = (
            'age'
            'user',
            'addres',
            'linkedin',
            'github',
        )
    def validate_addres(self ,data):
        #import pdb; pdb.set_trace()
        addres = self.data['addres']
        if type(addres) != str : 
            raise serializers.ValidationError('type of addres is string')
        elif len(addres) < 10 :
            raise serializers.ValidationError('the address is to short')
        return addres
    

    def validate_age(self, data):
        age = data['age']
        if type(age) != int :
            raise serializers.ValidationError('age minors not admited')
        if age < 18:
            raise serializers.ValidationError('age is minor of 18')"""