from rest_framework.serializers import ModelSerializer

from apps.api_users.serializers import ProfileSerializer
#models
from apps.users.models import CV ,Skills ,Experiences ,PersonalRef 


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields= '__all__'

class PersonalRefSerializer(ModelSerializer):
    class Meta:
        model=PersonalRef
        fields = '__all__'

class ExperiencesSerializer(ModelSerializer):
    class Meta:
        model=Experiences
        fields = '__all__'

class CvSerializer(ModelSerializer):
    skills=SkillSerializer(many=True , read_only=True)
    personal_ref = PersonalRefSerializer(many=True , read_only=True)
    experiences = ExperiencesSerializer(many=True , read_only=True)
    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = CV 
        fields = '__all__'