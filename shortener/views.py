from django.shortcuts import render, redirect
from django.http import HttpResponse
import urllib3
from django.views.decorators.csrf import csrf_exempt
from .models import URL
import uuid
import pymongo
from pymongo import MongoClient
import json
from decouple import config

client = MongoClient(config('MONGO'))
db = client[config('DATABASE')]
coll = db[config('COLLECTION_NAME')]
#tokendb = db[config('TOKENDB')]

def index(request):
    request.COOKIES['key'] = str(uuid.uuid1())
    response = render(request, 'home.html') 
    response.set_cookie('key', str(uuid.uuid1()))
    return response

def shorten(request):    
    if request.method == 'POST':
        user = request.COOKIES.get('key')
        url = request.POST['link']
        if url.find('<name of your domain>') != -1:
            return render(request, 'home.html', {'status': 'Funny'})
        http = urllib3.PoolManager()
        valid = False
        if url.startswith("http"):            
            url = url    
        else:
            url = "http://"+url
        
        try:
            ret = http.request('GET',url)
            if ret.status == 200:
                valid = True
        except Exception as e:
            valid = False
            
        if valid == True:
            new_url = str(uuid.uuid4())[:5]
            surl = "<name of your domain>"+new_url
            sch = {'uid' : user, 'link' : url, 'new' : surl}
            coll.insert_one(sch)
            return render(request, 'final.html', {'user':user, 'url': url, 'new':surl})           #dynamic data onto your HTML template
        else:
            return render(request, 'home.html', {'status': False})
    return redirect('/')
