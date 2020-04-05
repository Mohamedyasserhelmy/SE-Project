from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from homepage.models import User
from .forms import user_form, reg_form
from .serializers import userSerializer
from rest_framework import viewsets, permissions


# Create your views here.

class userViewSet(viewsets.ModelViewSet):
      serializer_class = userSerializer
      queryset = User.objects.all()
      permission_classes = [permissions.IsAuthenticated]


class HomePageView(TemplateView):
    template_name = 'index.html'

class LoginView(FormView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = user_form
    def __init__(self):
        name = None
        
    
    
    def form_valid(self, form):
        
        self.name = form.cleaned_data['username']
        pas  = form.cleaned_data['password']
        ans  =  User.objects.filter(username = self.name, password = pas)
        
        if ans.exists():
            vp = [item.password for item in ans]
            vid = [item.id for item in ans]

            sess = self.request.session.get('id')
            if vp[0] == pas and sess != vid[0]:
                self.request.session['name'] = self.name
                self.request.session['id'] = vid[0]
                return HttpResponseRedirect(reverse_lazy('home'))
            else:
                return HttpResponseRedirect(reverse_lazy('login'))
        else:
            return HttpResponseRedirect(reverse_lazy('login'))    
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        print(self.request.session.get('id'))
        return HttpResponseRedirect(reverse_lazy('login'))        

class RegForm(FormView):
    template_name = 'registeration.html'
    form_class = reg_form
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        add = form.cleaned_data['address']
        cat = form.cleaned_data['category']
        user = User(username = name, email = email,password= password,
         address = add, Type = cat)
        user.save()
        return super(RegForm, self).form_valid(form)

