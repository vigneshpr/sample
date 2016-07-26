from django.http import HttpResponse
import datetime
from django.template import Context, Template
from django.shortcuts import render
from django.shortcuts import render_to_response

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)



def index_test(request):
	f = open('/home/local/TAG/vigneshwarann/html/main.html', 'r+')
  	return HttpResponse(f)
def index_test1(request):
    return HttpResponse("<h1>Hello, world. You're at the index_test1 index.</h1><br><h2>Welcome</h2>")
def index_test2(request):
    return HttpResponse("<h1>Hello, world. You're at the index_test2 index.</h1><br><h2>Welcome</h2>")
def index_test3(request):
	#return HttpResponse("<h1>Hello, world. You're at the index_test2 index.</h1><br><h2>Welcome</h2>")
    #print("demo")
    now = datetime.datetime.now()
    name="django"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,'polls/index.html', {'now' : now,'name':name ,'age':BASE_DIR})

    #the above lines refers that the request is directly redirected to the polls/index.html 
    #{'now' : now,'name':name ,'age':BASE_DIR} refers a dict where "now ,name,age" refers to the context variable that #should be same with the html file
    
    #return render(request, 'blog/post_detail.html', {'post': post})