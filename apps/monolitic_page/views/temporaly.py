#django
from django.shortcuts import render
#models
from apps.users.models import Profile , CV
#from django.views.generic import TemplateView , ListView


def TemporalyView(request) :

    profile=Profile.objects.get(is_cv_porter=True)
    cv = CV.objects.get(profile=profile)
    context = {
        'profile':profile,
        'cv':cv ,
        'skills':cv.skills.all(),
        
        
    }
    #import pdb; pdb.set_trace()
    return render(request,template_name='index.html' , context=context)
    