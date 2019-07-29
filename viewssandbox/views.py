from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserInfo
import datetime


# just a simple view with some html text
def simple(request):
  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')

# a simple Function Based LIST View with template
def fbvlist(request):
    total_users = UserInfo.objects.all()

    context = {
        'total_users': total_users,
    }

    return render(request, 'viewssandbox/FBVlist.html', context=context)

class UserInfoListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_list.html'


