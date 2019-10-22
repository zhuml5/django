from django.shortcuts import render
import re
import socket
from .models import User
from .models import Post
from django.db.models import Q
# Create your views here.
def index(request):
    print('1')
    ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    print(ip)
    user_list = User.objects.all()
    print(user_list.query)
    list = []
    for i in user_list:
         list.append(i.mn)
    return render(request, 'index.html', {'index_list':list,'ip':ip})

def display(request):
    mn_c = request.GET.get('mn')
    num = request.GET.get('num')
    print(mn_c)
    print(num)
    post_list = Post.objects.filter(mn = mn_c)[:num]
    for i in post_list:
         print(i)
    return render(request, 'display.html', {'realtime_data1':list})

def textpost(request):
    if request.method == 'POST':
        return render(request, 'display.html', {'realtime_data1':list})
    else:
        ip = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
        user_list = User.objects.all()
        list = []
        for i in user_list:
             list.append(i.mn)
        return render(request, 'index.html', {'index_list':list,'ip':ip})
