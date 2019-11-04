#rest framework
from rest_framework import serializers 

#models
from apps.users.models import Skills

class SkillsOwnerCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields=(
            'id',
            'name',
            'description'
        )
