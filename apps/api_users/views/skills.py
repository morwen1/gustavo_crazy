#Models
from apps.users.models import CV , Skills ,  PersonalRef 

#Serializers
from apps.api_users.serializers import CvSerializer , SkillSerializer ,PersonalRefSerializer

#Rest Framework
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
# Filters
from rest_framework.filters import SearchFilter, OrderingFilter




class SkillsViewset(ReadOnlyModelViewSet):
    """
        listing skills with ordering and filters *ordering* , *search*
    """
    
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ('name' , )
    ordering_fields =('pt' , 'name')


    def dispatch(self , request , *args , **kwargs):
        id = kwargs['id']
        self.cv = CV.objects.get(id=id)
        return super(SkillsViewset ,self).dispatch(request , *args , **kwargs)
    
    serializer_class=SkillSerializer
    def get_queryset(self , *args , **kwargs):
        queryset = self.cv.skills.all()
        return queryset
