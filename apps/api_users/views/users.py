#Rest framework
from rest_framework.viewsets import mixins , GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#Serializers
from apps.ap_users.serializers import UsersSerializer , UsersLoginSerializer , UserSignupSerializer

#Models
from apps.users.models import Users


class UserList (GenericViewSet,mixins.ListModelMixin , mixins.RetrieveModelMixin):
    queryset=Users.objects.all()
    serializer_class = UsersSerializer
    

    @action(detail=False , methods=['post'])
    def login(self , request):
        serializer = UsersLoginSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        user , token = serializer.save()
        data = {
            'user':UsersSerializer(user).data,
            'token':token
        }
        return Response (data , 200)
    
  
    @action(detail=False , methods=['post'])
    def signup(self, request):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response(UsersSerializer(user).data , 200)
            
]