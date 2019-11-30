from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from personal import settings

urlpatterns = [
   # path('blogs/', views.PostList.as_view(), name="writings"),
    path('blogs/', views.PostList, name="writings"),
    path('blogs/<slug:slug>/',views.PostDetail,name='post_detail'),
    path('contact/',views.contact, name="contact"),
    path('resume/',views.cv, name="resume"),
    path('', views.home, name="blog-home"),
    # path('search/',views.search,name='search'),
    path('ckeditor/',include('ckeditor_uploader.urls'))
   
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
