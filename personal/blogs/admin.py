from django.contrib import admin

# Register your models here.
from .models import post, Categories, Author, Contacted, Comment
#from .forms import ContactForm

#admin.site.register(post)
admin.site.register(Categories)
admin.site.register(Author)
#admin.site.register(Contacted)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('Name','Email','Comment')

@admin.register(Contacted)
class ContactedAdmin(admin.ModelAdmin):
    list_display=('Name','Email')

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'Address','Published_on','updated_on')
    list_filter =("status",)
    search_fields = ['title','content']
    prepopulated_fields = {'slug':('title',)}