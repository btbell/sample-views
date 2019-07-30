from django.shortcuts import render

from .forms import ContactForm

def form_test(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      pass  # does nothing, just trigger the validation
  else:
    form = ContactForm()
  return render(request, 'viewssandbox/user_form.html', {'form': form})



