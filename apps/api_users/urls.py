
from django.urls import path , include
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from apps.api_users.views import (
    UserList , ProfileViewset, 
    CommentsViewset , CViewset , 
    SkillsViewset
)

router = SimpleRouter()

router.register(r'cv' , CViewset , base_name='cv')
router.register(r'comments' , CommentsViewset, base_name='coments')
router.register(r'users' ,UserList, base_name='users')
router.register(r'profiles' , ProfileViewset , base_name='profile')
router.register(r'cv/(?P<id>[-0-_9])/skills2' , SkillsViewset , base_name='skills')
urlpatterns = [
    path('users/loginjwt/' , TokenObtainPairView.as_view() ,name='jwtloggin'),
    path('users/refreshjwt/' , TokenRefreshView.as_view() , name='jwtrefresh'),
    
    path('' , include( router.urls)),
 ]
