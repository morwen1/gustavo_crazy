from django.urls import path , include
from apps.monolitic_page.views import TemporalyView

urlpatterns=[
    path('' , TemporalyView , name='index')

]