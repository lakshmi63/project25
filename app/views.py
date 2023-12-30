from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        to.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
    

        return render(request,'display_topic.html',d)
    return render(request,'topic.html')

def webpage(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        n=request.POST['n']
        u=request.POST['u']
        em=request.POST['em']
        to=Topic.objects.get_or_create(topic_name=tn)[0]
        wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u,email=em)[0]
        wo.save()

        WLTO=Webpage.objects.all()
        d1={'webpages':WLTO}




        return render(request,'display_webpage.html',d1)
    return render(request,'webpage.html',d)


def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'data1':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d2={'webpages':QLWO}
        return render(request,'display_webpage.html',d2)
    return render(request,'select_multiple_webpage.html',d)
