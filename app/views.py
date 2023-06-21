from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app.models import *

def insert_topic(request):
    tn=input('Enter Topic Name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('Topic is inserterd')



def insert_webpage(request):
    tn=input('Enter Topic Name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name')
    u=input('Enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('Webpage data inserted')


def insert_accessrecords(request):
    tn=input('Enter Topic Name')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('Enter name')
    u=input('Enter url')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    a=input('enter author name')
    d=input('Enter the date')
    AR=AccessRecords.objects.get_or_create(name=WO,author=a,date=d)[0]
    AR.save()
    return HttpResponse('accessrecords data inserted')
    

