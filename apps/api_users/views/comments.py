#Rest Framework
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter



#Models
from django.db.models import Prefetch
from apps.api_users.models import CommentSkill 

#Serializers
from apps.api_users.serializers import CommentsSerializers ,CommentsSerializersCreate






class CommentsViewset(
                mixins.ListModelMixin ,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin ,
                GenericViewSet
                                ):


    """
    Comments view :
        this view is for send comments to my cv ,
        one comment have many comments, 
        params :
            offset = pagination,
            filtering
            ordering
        actions:
            list:
                api/v1/comments/
            
            retrieve:
                api/v1/comments/{id}
            
            create:
                method : POST 
                api/v1/comments/

            reply:
                method : POST 
                api/v1/comments/{id}/reply/

    """
    
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ('text',)
    ordering_fields = ('likes' , 'id')
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        
        
        if self.action == 'list':
            queryset = CommentSkill.objects.filter(reply=False)
           
        if self.action in [ 'retrieve','create','reply','update','partial_update']:
            queryset = CommentSkill.objects.all()
        queryset.prefetch_related(
                Prefetch('Comments')
            )
        
        return queryset
    
    def get_serializer_class(self):
        if self.action in [ 'create' , 'reply' , 'update', 'partial_update'] :
            return CommentsSerializersCreate
        else :
            return CommentsSerializers
        
    
    @action(detail=True , methods =['post'])
    def reply (self , request , pk=None):
        """
            reply
                is only for reply comments
                
        """
        partial = request.method == 'PATCH'
        serializer = CommentsSerializersCreate(
            data=request.data , 
            context=self.get_serializer_context() , 
            partial=partial
            )
        serializer.is_valid(raise_exception=True)
        rply = serializer.save()
        rply.reply=True
        rply.save()
        comment = CommentSkill.objects.get(id=int(pk))
        
        
        dataresponse=CommentsSerializers(rply).data
        
        comment.coments.add(rply)
        dataresponse=CommentsSerializers(rply).data
        return Response(data=dataresponse ,status= 201)
        


    
    def perform_create(self, serializer):
        #import pdb; pdb.set_trace()
        data = self.request.data
        serializer_class = self.get_serializer_class()
        serializer = serializer_class( 
            data=data,
            context=self.get_serializer_context()
            )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data , status=201)


    