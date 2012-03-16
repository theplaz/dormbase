from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from dormbase.package.models import Package

def dashboard(request):
    payload = {'packages': Package.objects.all()}
    return render_to_response('desk/dashboard.html', payload, context_instance = RequestContext(request))
