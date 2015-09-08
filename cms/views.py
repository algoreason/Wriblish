from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import Post,Topic
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def home(request):
	topics= Topic.objects.all()
	if not request.user.is_authenticated():
		return render(request,'cms/ViewByIndex.html',{'topics':topics})
	username=request.session['user_idname']
	user=User.objects.get(username=username)
	return render(request,'cms/ViewByIndex.html',{'topics':topics,'username':user})

def posts(request,category_id):
	category=Topic.objects.get(id=category_id)
	posts=Post.objects.filter(topic=category)
	if not request.user.is_authenticated():
		return render(request,'cms/posts.html',{'topic':category,'posts':posts})
	username=request.session['user_idname']
	user=User.objects.get(username=username)
	context={'posts':posts,'topic':category,'username':user}
	return render(request,'cms/posts.html',context)

def loginInitialization(request):
	return render(request,'cms/login.html',{})

def login_proc(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            request.session['user_idname']=username
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("User Disabled")
    else:
    	return HttpResponseRedirect("/login/error")

def loginRetry(request,error):
    return render(request,'cms/login.html',{'error_message':'error'})

def addPostInit(request):
	topics=Topic.objects.all()
	if not request.user.is_authenticated():
		return render(request,'cms/addPost.html',{'topics':topics})
	username=request.session['user_idname']
	user=User.objects.get(username=username)
	return render(request,'cms/addPost.html',{'topics':topics,'username':user})

def savePost(request):
	heading=request.POST['heading']
	text=request.POST['text']
	topic=request.POST['topic']
	username=request.session['user_idname']
	user=User.objects.get(username=username)
	topics = Topic.objects.get(topic_name=topic)
	post = Post.objects.create(heading=heading,text=text,author=user,topic=topics);
	post.save()
	post.publish()
	return HttpResponseRedirect("/")

def logout_view(request):
    logout(request)
    request.session.flush
    return HttpResponseRedirect("/")

def register(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password=request.POST.get('password')
    first_name=request.POST.get('firstname')
    last_name=request.POST.get('lastname')
    user = User.objects.create_user(username,email,password)
    user.last_name = last_name
    user.first_name = first_name
    user.save()
    return HttpResponseRedirect("login/")

def registerInit(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	return render(request, 'cms/register.html', {})

def profileView(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    user=User.objects.get(username=request.session['user_idname'])
    context={'user':user}
    return render(request,'cms/profileView.html',context)