
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from genre.forms import UserForm
from . models import Collection,Piece
from django.views import generic 
from django.contrib.auth import authenticate,login
from django.views.generic import View


class genre_view(generic.ListView):
    form_class = UserForm
    template_name="genre/genretemplate.html"

    def get_queryset(self):
        return Collection.objects.all()



class details(generic.DeleteView):
    model=Collection
    form_class = UserForm
    template_name="genre/detailtemplate.html"


class UserFormView(View):
    form_class=UserForm
    template_name='genre/formtemplate.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})
    
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()

            newuser=authenticate(username=username,password=password)

            if newuser is not None:
                if newuser.is_active:
                    login(request,newuser)
                    return redirect(reverse('genre'))
    
        return render(request,self.template_name,{'form':form})