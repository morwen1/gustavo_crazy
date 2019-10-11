from apps.users.models import Profile ,Users
from rest_framework.authtoken.models import Token

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth import password_validation, authenticate





class UsersSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )




class UserSignupSerializer(serializers.Serializer):
    """
         SERIALIZER FOR REGISTER USERS
    """
    email = serializers.EmailField()
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    password_verif = serializers.CharField(max_length = 255)
    first_name =  serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    def validate (self , data):
        passwd = data['password']
        password_verif = data['password_verif']
        if passwd != password_verif : 
            raise serializers.ValidationError('passwords does not equals')
        else:
            password_validation.validate_password(passwd)
        return data

    def create(self , data):
        data.pop('password_verif')
        age = data.pop('age')
        user = Users.objects.create_user(
            **data,
            is_verified=True
        )

        Profile.objects.create(user=user,
                is_cv_porter=False,
                is_admin=False ,
                age=age
                )
        return user
    



class UsersLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)

    def validate(self , data):
        user = authenticate(email = data['email'] , password = data['password'])
        if not user:
           raise serializers.ValidationError('this user not exist')
        else : 
            self.context['user'] = user
        return data

    def create(self, data):
        token ,created = Token.objects.get_or_create(user = self.context['user'])
        return self.context['user'] , token.key