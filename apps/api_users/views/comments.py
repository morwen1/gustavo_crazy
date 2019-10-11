#Rest Framework
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter




#Models

from apps.api_users.models import CommentSkill 

#Serializers
from apps.api_users.serializers import CommentsSerializers ,CommentsSerializersCreate



class CommentsViewset(
                mixins.ListModelMixin ,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                GenericViewSet
                                ):


    """
    Comments view :
        this view is for send comments to my cv ,
        one comment have many comments 

    """
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ('text',)
    ordering_fields = ('likes' , 'id')
    
    queryset = CommentSkill.objects.filter(reply=False)

    def get_serializer_class(self):
        if self.request.method != 'POST' :
            serializer_class = CommentsSerializers
        else :
            serializer_class=CommentsSerializersCreate
        return serializer_class

    @action(detail=True , methods =['post'])
    def reply (self , request , pk=None):
        serializer = CommentsSerializersCreate(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = CommentSkill.objects.get(id=int(pk))
        rply = serializer.save()
        rply.reply=True
        rply.save()
        comment.coments.add(rply)
        #import pdb; pdb.set_trace()
        dataresponse=CommentsSerializers(rply).data
        return Response(data=dataresponse ,status= 201)

    

    #@ction(detail=True,methods='')

    