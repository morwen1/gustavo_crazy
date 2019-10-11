from django.contrib import admin

# Register your models here.
from .models import CV ,Profile, Users , Skills ,PersonalRef , Experiences

admin.site.register(Skills)
admin.site.register(PersonalRef)
admin.site.register(Experiences)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id' , 'user' , 'age'  , 'cellphone' ,'is_cv_porter')
    list_display_links = ('id','user')
    list_editable = ('age' , 'cellphone')
    search_fields=(
        'user__username',
        'user__email',
        'cellphone'
    )
    list_filter=(
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'id',
    
        )
        


@admin.register(CV)
class CVadmin(admin.ModelAdmin):
    list_display=('profile' ,)
    list_filter=(
        'profile__user__username',
        'profile__user__email',
        'profile__user__first_name',
        'profile__user__last_name',
       
        )
    search_fields=(
            'profile__user__username',
            'profile__user__email',
            'id',
        )








@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display=('id' , 'username' , 'password' , 'email')
    search_fields= ('id' ,'email','username') 


