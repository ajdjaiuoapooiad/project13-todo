from django.shortcuts import redirect,render
from .models import Post
from django.views import generic
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin,generic.ListView):
    model=Post
    login_url = 'todo:login'
    
class DetailView(generic.DetailView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('todo:index')
    
class DeleteView(generic.DeleteView):
    model=Post
    success_url=reverse_lazy('todo:index')
    
class UpdateView(generic.UpdateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('todo:index')
    

def signupview(request):
    if request.method=='POST':
        username2=request.POST['username']
        password2=request.POST['password']
        try:
            User.objects.get(username=username2)
            return render(request,'todo/signup.html',{'error':'このユーザーは登録されています'})
        except:
            user=User.objects.create_user(username2,'',password2)
            return render(request,'todo/login.html',{'some':100})
    return render(request,'todo/signup.html',{'some':100})

def loginview(request):
    if request.method=='POST':
            username2=request.POST['username']
            password2=request.POST['password']
            user=authenticate(request,username=username2,password=password2)
            if user is not None:
                login(request,user)
                return redirect('todo:index')
            else:
                return redirect('todo:login')
    return render(request,'todo/login.html')

def logoutview(request):
    logout(request)
    return redirect('todo:login')

def goodview(request,pk):
    post = Post.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.usertext:
        return redirect('todo:index')
    else:
        post.good+= 1
        post.usertext= post.usertext + ' ' + post2 #usertextにusernameとスペースを入れていく
        post.save()
        return redirect('todo:index')
     
    