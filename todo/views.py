from django.shortcuts import redirect,render
from .models import Post
from django.views import generic
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    model=Post
    
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
        username2=request.POST('username')
        password2=request.POST('password')
        try:
            User.objects.get(username=username2)
            return render(request,'todo/signup.html',{'error':'このユーザーは登録されています'})
        except:
            user=User.objects.create_user(username2,'',password2)
            return render(request,'todo/signup.html',{'some':100})
    return render(request,'todo/signup.html',{'some':100})
    