from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader


# Create your views here.

def home(request):
    template=loader.get_template('home/index.html')
    context=RequestContext(request, {})
    return HttpResponse(template.render(context))