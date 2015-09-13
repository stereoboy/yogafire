from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Pose

def view_poses(request, pose_name):
    return HttpResponse("Hello, Here is the yogafire poses viewer. " + pose_name)

def view_poses_all(request):
    poses = Pose.objects.all()
    template = loader.get_template('./poses.html')
    context = RequestContext(request, { 'poses': poses, })
    return HttpResponse(template.render(context))
