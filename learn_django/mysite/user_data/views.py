from django.shortcuts import render

from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from .models import user_data

from .forms import user_details

from django.views import generic

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


# class IndexView(generic.ListView):
#     model = user_data
#     template_name = 'user_data/input_details.html'
@login_required
def index(request):
    return render(request,'user_data/index.html')    


class view_details(LoginRequiredMixin, generic.ListView):
    context_object_name = 'userdata'
    template_name = 'user_data/view_details.html'
    def get_queryset(self):
        return user_data.objects.filter(user=self.request.user)

@login_required
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_details(request.POST, request.user)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            n = form.cleaned_data['name']
            t = form.cleaned_data['town']
            a = form.cleaned_data['age']
            u = user_data(full_name=n, home_town=t, age=a)
            u.user = request.user
            u.save()
            messages.success(request, ('User Details Updated'))
            return HttpResponseRedirect('/user_data/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = user_details()

    return render(request, 'user_data/input_details.html', {'form': form})