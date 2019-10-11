from rest_framework.serializers import ModelSerializer
from apps.users.models import Profile
from .users import UsersSerializer

class ProfileSerializer(ModelSerializer):
    user = UsersSerializer(read_only=True)
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