from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
#from django.views.generic.edit import CreateView, UpdateView, DeleteView

import datetime


# just a simple view with some html text
def simple(request):
  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')