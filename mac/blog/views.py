from django.shortcuts import render
from django.http import HttpResponse
from .models import vlogpost
# Create your views here.


def index(request):  
    myposts = vlogpost.objects.all()
    return render(request,"blog/index.html", {'myposts': myposts})
def blogpost(request, id):
    post = vlogpost.objects.filter(post_id = id)[0]
    print(post)    
    return render(request,"blog/blogpost.html", {'post':post})