#DJANGO
from django.urls import path , include

#REST FRAMEWORK
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView

#VIEWS
from apps.api_users.views import (
    #viewsets for everybody
    UserList , ProfileViewset, 
    CommentsViewset , CViewset , 
    SkillsViewset ,
    #viewsets for *dueños of cv
    SkillsOwnerViewset,
    ReferOwnerVieset , 
    ExperiencesOwnerViewset
)

router = SimpleRouter()


#ROUTER REGISTER
router.register(r'cv' , CViewset , base_name='cv')
router.register(r'comments' , CommentsViewset, base_name='coments')
router.register(r'users' ,UserList, base_name='users')
router.register(r'profiles' , ProfileViewset , base_name='profile')
router.register(r'cv/(?P<id>[-0-_9])/skills2' , SkillsViewset , base_name='skills')
router.register(r'cv/owner_only/skills_owner' , SkillsOwnerViewset , base_name='owner_viewset')
router.register(r'cv/owner_only/refpers_owner' , ReferOwnerVieset , base_name='owner_refer')  
router.register(r'cv/owner_only/experiences_owner', ExperiencesOwnerViewset , base_name='owner_exp')



urlpatterns = [
    path('users/loginjwt/' , TokenObtainPairView.as_view() ,name='jwtloggin'),
    path('users/refreshjwt/' , TokenRefreshView.as_view() , name='jwtrefresh'),
    
    path('' , include( router.urls)),
 ]
