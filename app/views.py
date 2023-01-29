from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        T = Topic.objects.get_or_create(topic_name = tn)[0]
        T.save()
        return HttpResponse ('<h1>Topic model inserted successfully!</h1>')
    return render(request, 'insert_topic.html')

def insert_webpage(request):
    if request.method == 'POST':
        tn = request.POST['tn']
        name = request.POST['name']
        url = request.POST['url']
        T = Topic.objects.get_or_create(topic_name = tn)[0]
        T.save()
        W = Webpage.objects.get_or_create(topic_name = T, name = name, url = url)[0]
        W.save()
        return HttpResponse ('<h1>Webpage model inserted successfully!</h1>')        
    return render(request, 'insert_webpage.html')

def insert_access(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        W = Webpage.objects.get_or_create(name = name)[0]
        W.save()
        A = Access_Record.objects.get_or_create(name = W, date = date)[0]
        A.save()
        return HttpResponse ('<h1>Access_Record model inserted successfully!</h1>')
    return render(request, 'insert_access.html')