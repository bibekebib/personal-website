from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from .forms import ContactForm
from .models import Contacted, Comment
from .models import post
from django.views import generic
from django.core.paginator import Paginator


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

'''def contact2(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('') # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'home.html', {'form': form})'''
'''def reply(request):
    if request.method=='POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog/<slug:slug>/')
    else:
        form = ReplyForm()
    return redirect('/blog/<slug:slug>as_view')'''

'''def PostList(request):
    queryset = post.queryset = post.objects.filter(status=1).order_by('-Published_on')
    context = {
        'posts':posts,

    }'''
    
#class PostList(generic.ListView):
 #   queryset = post.objects.filter(status=1).order_by('-Published_on')
  #  template_name = 'blogs.html'
def PostList(request):
    material = post.objects.all()
    
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/blog') # does nothing, just trigger the validation
    # else:
    #     form = ContactForm()
    
    
    return render(request, 'blogs.html', {'material':material})

def PostDetail(request, slug):
    this = post.objects.all()
    material = post.objects.get(slug= slug)
    return render(request, 'post_detail.html',{'material':material,'this':this})

# def search(request):
#     search_term = request.GET.get('title_contains')

#     # if 'search' in request.GET:
#     #     search_term = request.GET['search']
#     #     articles = post.objects.all().filter(title_contains=search_term) 

#     articles = post.objects.all()

#     return render(request, 'search.html', {'articles' : articles, 'search_term': search_term })
#class PostDetail(generic.DetailView):
 #   model = post
  #  template_name = 'post_detail.html'
