from rest_framework.viewsets import GenericViewSet ,mixins
from rest_framework.permissions import IsAuthenticated , IsAuthenticatedOrReadOnly
from apps.users.models import Profile
from django.db.models import Q
from django.db.models import Prefetch
from apps.api_users.serializers import ProfileSerializer 
from rest_framework.decorators import action
from rest_framework.response import Response

class ProfileViewset(
     mixins.RetrieveModelMixin, 
     mixins.ListModelMixin , 
     GenericViewSet 
    ):
    
    """
        endpoint of list profiles for update your profile
        
            list:
                listing profiles
                /api/v1/profiles/
            
            retrieve:

                /api/v1/profiles/{id}/



            update profile:
                
                updating own profile
                /api/v1/profiles/updateprf
    """



    queryset = Profile.objects.filter(Q(is_admin=False)&Q(is_cv_porter=False))
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class= ProfileSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.prefetch_related(Prefetch('user'))
    
        return queryset
        
    @action(detail=False , methods=['put', 'patch'])
    def updateprf(self , request):
        
        user = request.user
        profile = Profile.objects.get(user=user)
        patch = request.method=='PATCH'
        serializer = ProfileSerializer(profile, data=request.data , partial = patch)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        