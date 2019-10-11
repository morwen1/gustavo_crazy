from rest_framework.viewsets import GenericViewSet ,mixins
from apps.users.models import Profile
from django.db.models import Q
from apps.api_users.serializers import ProfileSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProfileViewset(GenericViewSet , mixins.RetrieveModelMixin, mixins.ListModelMixin):
    queryset = Profile.objects.filter(Q(is_admin=False)&Q(is_cv_porter=False))
    serializer_class = ProfileSerializer
   
    @action(detail=False , methods=['put', 'post' , 'patch'])
    def updateprf(self , request):
        user = request.user
        #import pdb; pdb.set_trace()
        profile = Profile.objects.get(user=user)
        patch = request.method=='PATCH'
        serializer = ProfileSerializer(user, data=request.data , partial = patch)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
