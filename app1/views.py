from django.shortcuts import render,HttpResponse,Http404
import os
from django.conf import settings
# Create your views here.
def welcome(request):
    return HttpResponse("welcome")
def download(request, id):
    file_path = os.path.join(settings.MEDIA_ROOT, str(id)+'.png')
    if os.path.exists(file_path):

        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="Content-Type: image/png")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    print(file_path," is not exists")
    raise Http404