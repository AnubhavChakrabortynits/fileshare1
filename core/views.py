from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.

from .models import File

def home(request):
    doc=""
    if(request.method=='POST'):
        myfile=request.FILES['files']
        print(myfile,type(myfile))
        doc=File.objects.create(file=myfile)
        doc.save()
        
        request.session['url']=doc.file.url
        return render(request,'home.html',{'file':f'/download{doc.file.url}/'})

    else:  
        return render(request,'home.html',{'file':doc})


def download(request,data,data1,data2):
    return render(request,'download.html',{'data':data,'data1':data1,'data2':data2
    })    