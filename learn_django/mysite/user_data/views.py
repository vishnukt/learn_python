from django.shortcuts import render

from django.http import HttpResponseRedirect

#from django.contrib.auth.models import User

from .models import user_data, User

from .forms import user_details

from django.views import generic

from django.contrib import messages
# Create your views here.


# class IndexView(generic.ListView):
#     model = user_data
#     template_name = 'user_data/input_details.html'
def index(request):
    return render(request,'user_data/index.html')    


class view_details(generic.ListView):
    # model = user_data
    context_object_name = 'userdata'
    template_name = 'user_data/view_details.html'
    def get_queryset(request):
        return User.objects.all()


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_details(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, ('User Details Updated'))
            return HttpResponseRedirect('/user_data')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = user_details()

    return render(request, 'user_data/input_details.html', {'form': form})