from rest_framework.permissions import AllowAny , IsAuthenticated , IsAuthenticatedOrReadOnly , BasePermission
from apps.users.models import Users , Profile



class Owner_cv (BasePermission):
    message = "user not cv porter , request rejected"
    def verif_owners(self , request, view):
        user =request.user
        owner = Profile.get(user=user).is_cv_porter
        return owner
    




class AllowAny_IsAuthenticated (Owner_cv):

    def get_permissions(self ):
        if self.request.method == 'GET':
            permissions = [AllowAny  , Owner_cv]
        else:
            permissions = [IsAuthenticated ,  IsAuthenticatedOrReadOnly, Owner_cv]
        
        return [p() for p in permissions]