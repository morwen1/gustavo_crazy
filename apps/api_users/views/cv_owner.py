#rest framework
from rest_framework import viewsets
from rest_framework.permissions import AllowAny , IsAuthenticated , IsAuthenticatedOrReadOnly

#serializers 
from apps.api_users.serializers import SkillsOwnerCVSerializer , CvSerializer , PersonalRefSerializer , ExperiencesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

#models
from apps.users.models import Profile , CV 

#utils 
from utils.mixins_permisions import AllowAny_IsAuthenticated





class SkillsOwnerViewset( AllowAny_IsAuthenticated,viewsets.ModelViewSet ):
    """
        viewset a charge of the skills of the owner of cv
        only a owner cv have acces of the skills
    """


    def get_queryset(self):

        user = self.request.user
        profile = Profile.objects.get(user=user )
        if profile.is_cv_porter==False:
            return {}
        else:
            cv = CV.objects.get(profile = profile)
            queryset = cv.skills.all()
    
        return queryset
    

    serializer_class = SkillsOwnerCVSerializer
    
class ReferOwnerVieset(IsAuthenticated,viewsets.ModelViewSet):
    """
        eng:
        This viewsets is only for operations on cv  references personal,
        only the user have a cv
        esp:
        este viewset es solo para operaciones en cv referencias personales ,
        solo para personas que tienen cv
    """
    
     
    def get_queryset(self):

        user = self.request.user
        profile = Profile.objects.get(user=user )
        if profile.is_cv_porter==False:
            return {}
        else:
            cv = CV.objects.get(profile = profile)
            queryset = cv.personal_ref.all()
    
        return queryset
    
    serializer_class = PersonalRefSerializer



class ExperiencesOwnerViewset(IsAuthenticated , viewsets.ModelViewSet):
    """
        this viewsets is for operations in Experiences only for admin user
    """
    
    
    
     
    def get_queryset(self):

        user = self.request.user
        profile = Profile.objects.get(user=user )
        if profile.is_cv_porter==False:
            return {}
        else:
            cv = CV.objects.get(profile = profile)
            queryset = cv.experiences.all()
    
        return queryset
    
    serializer_class= ExperiencesSerializer
