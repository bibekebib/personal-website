from django import forms
from django.shortcuts import render, redirect
from .models import Contacted
class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacted
        widgets= {
            'Name':forms.TextInput(attrs={'placeholder':'Name'}),
            'Email':forms.TextInput(attrs={'placeholder':'Email'}),
            'Subject':forms.TextInput(attrs={'placeholder':'Subject'}),
            'Message':forms.Textarea(attrs={'placeholder':'Your Message'})
        }
        fields=('Name','Email','Subject','Message')
   # Name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Full Name'}), required=True)
    #Email = forms.EmailField(label="Your Email", required=True,widget=forms.TextInput(attrs={'placeholder':'Email'}))
    #Subject = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Subject'}))
    #Messsage = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder':'Your Message'}))


