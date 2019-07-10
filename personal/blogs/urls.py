from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.PostList.as_view(), name="writings"),
    path('blogs/<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),
    path('contact/',views.contact, name="contact"),
    path('resume/',views.cv, name="resume"),
    path('', views.home, name="blog-home")
   
]
