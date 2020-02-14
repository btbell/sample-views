from django.shortcuts import render
#from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import UserInfo, DogInfo, Reporter, Article, Tutorial
from .forms import UserForm, DogInfoForm
from django.db.models import Q
from django_tables2 import SingleTableView, RequestConfig
from .tables import UserTable, UserInfoTable
#import datetime

# # # LANDING page for the views sandbox # # #
def landing(request):

  return render(request, 'viewssandbox/landing.html')

# # # just a SIMPLE view with some html text # # #
def simple(request):

  return HttpResponse('This is simple view with some text returned using the HttpResponse method and a text string.')


def test(request):

  return render(request, 'viewssandbox/formtest.htmlNOTUSED')

# # # FUNCTION-Based View examples # # #
# simple Function-Based LISTView with template INCLUDING Search
def fbvlist(request):
  query = request.GET.get('q', None)
  total_users = UserInfo.objects.all()
  if query is not None:
      # Q returns an object so you can make more complex searches - See Q and Django
      total_users = total_users.filter(
          Q(first_name__icontains=query) | Q(last_name__icontains=query)
      )
  context = {
      'total_users': total_users,
  }

  return render(request, 'viewssandbox/FBV_list.html', context=context)

# Filtered, Sortable Function-based Listview
def fbv_filtered_sort_list(request):
  table = (UserInfoTable(UserInfo.objects.filter(status__exact='Professional')))
  # sort no worky without request config!
  RequestConfig(request).configure(table)

  return render(request, 'viewssandbox/FBV_filtered_sortable_list.html', {
    "table": table
  })


def form_test(request):
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = UserForm()
  return render(request, 'viewssandbox/user_form.html', {'form': form})

# dog/owner form - simple form
def model_form_test(request):
  if request.method == 'POST':
    form = DogInfoForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = DogInfoForm()
  return render(request, 'viewssandbox/model_user_form.html', {'form': form})

# # # CLASS-Based View examples # # #

# simple class-based view
class UserInfoListView(generic.ListView):
  model = UserInfo
  template_name = 'viewssandbox/CBV_list.html'

# simple CBV listview using Django-tables2 to give sortable columns
class UserInfoSortableListView(generic.ListView):
  model = UserInfo
  template_name = 'viewssandbox/CBV_sortable_list.html'


# simple CBV listview using Django-tables2 AND excluding columns
class UserInfoCustomSortableListView(SingleTableView):
  model = UserInfo
  table_class = UserTable
  template_name = 'viewssandbox/CBV_custom_sortable_list.html'

# simple CBV FILTERED listview using Django-tables2 AND excluding columns
class UserInfoFilteredSortableListView(SingleTableView):
  model = UserInfo
  table_class = UserTable
  template_name = 'viewssandbox/CBV_filtered_sortable_list.html'

# simple listview with a search function using Q objects
class UserSearchListView(generic.ListView):
  model = UserInfo
  template_name = 'viewssandbox/CBV_search.html'

  # Q objects for search function
  def get_queryset(self):  # new
    query = self.request.GET.get('q')
    object_list = UserInfo.objects.filter(
      Q(first_name__icontains=query) | Q(last_name__icontains=query)
    )
    return object_list

# reporter listview
class ReporterListView(generic.ListView):
  model = Reporter
  template_name = 'viewssandbox/reporter_list.html'

class ReporterDetailView(generic.DetailView):
  # when you need to override a method in a CBV, you'll need to comment out model and template and build
  # your own method - in this case, to get a FK object, you need both tables in the query
  #model = Reporter
  #template_name = 'viewssandbox/reporter_detail.html'

  context_object_name = 'reporter'
  queryset = Reporter.objects.all()

  # get all articles related to a reporter
  context = Reporter.objects.get(id=1).article_set.all()

  def get_context_data(self, **kwargs):
    # call the base implementation (query) to get a context
    context = super().get_context_data(**kwargs)
    # add the queryset of all articles
    context['article'] = Article.objects.all()
    return context


class ArticleListView(generic.ListView):
  model = Article
  template_name = 'viewssandbox/article_list.html'

class ArticleDetailView(generic.DetailView):
  model = Article
  template_name = 'viewssandbox/article_detail.html'

#### Tutorial Views ####
class TutorialListView(generic.ListView):
  model = Tutorial
  template_name = 'viewssandbox/tutorial_list.html'

class TutorialDetailView(generic.ListView):
  model = Tutorial
  template_name = 'viewssandbox/tutorial_detail.html'