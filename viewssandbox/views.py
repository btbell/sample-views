from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserInfo, DogInfo
from .forms import UserForm, DogInfoForm
#import datetime

# landing page for the views sandbox
def landing(request):

    return render(request, 'viewssandbox/landing.html')

# just a simple view with some html text
def simple(request):

  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')

def test(request):

    return render(request, 'viewssandbox/formtest.htmlNOTUSED')

# a simple Function Based LIST View with template
def fbvlist(request):
    total_users = UserInfo.objects.all()

    context = {
        'total_users': total_users,
    }

    return render(request, 'viewssandbox/FBVlist.html', context=context)

def form_test(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = UserForm()
  return render(request, 'viewssandbox/user_form.html', {'form': form})

# dog/owner form
def model_form_test(request):
  if request.method == 'POST':
    form = DogInfoFormForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = DogInfoForm()
  return render(request, 'viewssandbox/model_user_form.html', {'form': form})

class UserInfoListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_list.html'




