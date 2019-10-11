from apps.users.models import Profile
from django.views.generic import TemplateView



class TemporalyView(TemplateView)  :
    template_name='index.html'
    