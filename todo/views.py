from django.shortcuts import redirect
from .models import Post
from django.views import generic
from .forms import PostCreateForm
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model=Post
    
class DetailView(generic.DetailView):
    model=Post
    
class CreateView(generic.CreateView):
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy('todo:index')
    
