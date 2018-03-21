from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context={}
    template = loader.get_template('corp/index.html')
    return HttpResponse(template.render(context, request))
