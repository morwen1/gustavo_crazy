from django.shortcuts import render
from django.utils.safestring import mark_safe
# Create your views here.
from django.shortcuts import render
import json

def index(request):
    return render(request,'chat.html')

def room(request, room_name):
    return render(request, 'room.html', {
    'room_name_json': mark_safe(json.dumps(room_name))
    })