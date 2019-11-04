#Django
from django.utils.decorators import method_decorator 
from django.views.decorators.cache import cache_page
#Models
from apps.users.models import CV , Skills ,  PersonalRef 

#Rest Framework
from rest_framework.viewsets import ReadOnlyModelViewSet 
from rest_framework.decorators import action
from rest_framework.response import Response

#Serializers1:M 25 Oct 13:15:08.475 * The server is now ready to accept connections on port 6379

from apps.api_users.serializers import CvSerializer , SkillSerializer ,PersonalRefSerializer




class CViewset(ReadOnlyModelViewSet ):
    """
        Viewset for my cv list the skills,
        experiencies and personal references
    """
    queryset = CV.objects.all()
    serializer_class =CvSerializer
    @method_decorator(cache_page(60*3))
    @action(detail=True , methods = ['get'])
    def skills (self,request,pk=None):
        """
            list only the skills relacionado* with one cv
        """
        cv = CV.objects.get(id=int(pk))
        skills = cv.skills.all()
        serializer = SkillSerializer(skills , many=True)
        return Response(data=serializer.data  ,status= 200)
    @method_decorator(cache_page(60*3))
    @action(detail=True , methods=['get'])
    def refper(self, request, pk=None):
        """
        list only personal references
        """
        cv = CV.objects.get(id=int(pk))
        peref = cv.personal_ref.all()
        serializer = PersonalRefSerializer(peref, many=True)
        return Response(data=serializer.data, status=200)
    


    
