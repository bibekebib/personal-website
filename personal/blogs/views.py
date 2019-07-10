from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .forms import ContactForm
from .models import Contacted
from .models import post
from django.views import generic


# Create your views here.

def home(request):
    return render(request, 'home.html')

def cv(request):
    return render(request, 'resume.html')
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact') # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


class PostList(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-Published_on')
    template_name = 'blogs.html'

class PostDetail(generic.DetailView):
    model = post
    template_name = 'post_detail.html'
