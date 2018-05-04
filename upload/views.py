from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .upload import upload

from .models import Voter


def index(request):
    voterlist = Voter.objects.order_by('-pub_date')[:5]
    template = loader.get_template('upload/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def simple_upload(request):
    
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        print(myfile)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        upload(uploaded_file_url)
        return render(request, 'upload/index.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload/index.html')