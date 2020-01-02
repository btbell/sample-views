from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
#from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserInfo, DogInfo, Reporter, Article
from .forms import UserForm, DogInfoForm
from django.db.models import Q
#import datetime

# landing page for the views sandbox
def landing(request):

    return render(request, 'viewssandbox/landing.html')

# just a simple view with some html text
def simple(request):

  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')


def test(request):

    return render(request, 'viewssandbox/formtest.htmlNOTUSED')


# a simple Function Based LIST View with template INCLUDING Search
def fbvlist(request):
    query = request.GET.get('q', None)
    total_users = UserInfo.objects.all()
    if query is not None:
        # Q returns and object so you can make more complex searches - See Q and Django
        total_users = total_users.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    context = {
        'total_users': total_users,
    }

    return render(request, 'viewssandbox/FBV_list.html', context=context)


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
    form = DogInfoForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = DogInfoForm()
  return render(request, 'viewssandbox/model_user_form.html', {'form': form})

# Class Based View example
class UserInfoListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_list.html'

class UserInfoSortableListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_sortable_list.html'

class UserSearchListView(generic.ListView):
    model = UserInfo
    template_name = 'viewssandbox/CBV_search.html'
    #queryset = UserInfo.objects.filter(first_name__icontains='hannah')  # new

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = UserInfo.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
        return object_list

class ReporterDetailView(generic.DetailView):
    model = Reporter
    template_name = 'viewssandbox/reporter_detail.html'

class ArticleDetailView(generic.DetailView):
    model = Article



