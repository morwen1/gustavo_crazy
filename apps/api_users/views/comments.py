#Rest Framework
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly

# Filters
from rest_framework.filters import SearchFilter, OrderingFilter



#Models
from django.db.models import Prefetch
from apps.api_users.models import CommentSkill , CommentsLikes

#Serializers
from apps.api_users.serializers import (CommentsSerializers ,
                                        CommentsSerializersCreate,
                                        CommentsLikesSerializers)






class CommentsViewset(
                mixins.ListModelMixin ,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin ,
                mixins.DestroyModelMixin,
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
                methods : POST 
                    api/v1/comments/

            reply:
                method : POST , DELETE 
                api/v1/comments/{id}/reply/
            
    """
    
    filter_backends = [SearchFilter , OrderingFilter]
    search_fields = ('text',)
    ordering_fields = ('likes' , 'id')
    
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):


        if self.action == 'destroy':
            queryset = CommentSkill.objects.filter(user_comment=self.request.user)
            return queryset

        if self.action == 'list':
            queryset = CommentSkill.objects.filter(reply=False)
           
        if self.action in [ 'retrieve','create','reply','update','partial_update']:
            queryset = CommentSkill.objects.all()
        
        queryset.prefetch_related(
                Prefetch('Comments')
            )
        
        return queryset
    """
    def destroy(self, request, *args , **kwargs):
        import pdb; pdb.set_trace()
        return super().destroy(request, *args , **kwargs)
"""
    def get_serializer_class(self):
        if self.action in [ 'create' , 'reply' , 'update', 'partial_update'] :
            return CommentsSerializersCreate
        else :
            return CommentsSerializers
        
    
    @action(detail=True , methods =['post'])
    def reply (self , request , pk=None):
        """
            reply is only for reply comments 
            
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
        
    @action(detail=True , methods=['post','delete',])
    def likes(self, request, pk=None):
        """
             like boton for coments *data is not required*
        """
        if request.method == 'POST':
            comment = CommentSkill.objects.get(id=int(pk))
            user_like = request.user
            valid =CommentsLikes.objects.filter(user=user_like,comment=comment)
            #import pdb; pdb.set_trace()
            if valid.count() > 0 :
                raise serializers.ValidationError('User alredy liked comment')

            try:
                like= CommentsLikes.objects.create(user=user_like,comment=comment)
            except:
                raise(serializers.ValidationError('User alredy liked comment'))
            
            
            like.save()
            serializer = CommentsLikesSerializers(like)
            serializer.data['status_like']='like is removed'
            return Response(data=serializer.data)
        if request.method == 'DELETE':
            comment = CommentSkill.objects.get(id=int(pk))
            user_like = request.user
            like= CommentsLikes.objects.filter(user=user_like,comment=comment).delete()
            serializer = CommentsLikesSerializers(like)
            serializer.data['status_like']='like is removed'
            return Response(data=serializer.data)


        
    
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


    