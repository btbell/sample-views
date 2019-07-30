from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserInfo

from .forms import UserForm
#import datetime


# just a simple view with some html text
def simple(request):
  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')

def test(request):

    return render(request, 'viewssandbox/formtest.html')

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

# user test form
def user(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check to see if it's valid
        if form.is_valid():
            pass # does nothing
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponse('/thanks')

        # if a GET (or any other method) we'll create a blank form
        else:
            form = UserForm()

    return render(request, 'user_form.html', {'form': form})

class UserInfoListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_list.html'




