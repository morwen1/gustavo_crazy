from django.urls import path , include
from apps.monolitic_page.views import TemporalyView

urlpatterns=[
    path('index/' , TemporalyView.as_view() , name='index')

]