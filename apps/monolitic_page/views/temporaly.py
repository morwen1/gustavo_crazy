#django
from django.shortcuts import render
from django.views.decorators.cache import cache_page
#models
from apps.users.models import Profile , CV
#from django.views.generic import TemplateView , ListView
from utils.peticiones.github import obtain_repos



#@cache_page(60*30)
def TemporalyView(request) :
    """
    falta:
        -obtener ultimos 10 post de linkedin
        -obtener ultimos 10 post de instagram
        -obtener los proyectos de github
        -ordenar mejor las urls de la api pública
        -logos de github y de todas mis skills
    """


    profile=Profile.objects.get(is_cv_porter=True)
    cv = CV.objects.get(profile=profile)
    context = {
        #'posts':get_posts(),
        #
        'repos':obtain_repos,
        'profile':profile,
        'cv':cv ,
        'skills':cv.skills.all(),

        
        
    }
    #import pdb; pdb.set_trace()
    return render(request,template_name='index.html' , context=context)
    