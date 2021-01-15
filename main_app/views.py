from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import InputForm
from .generateGraph import create_graph
from .tables import create_table

from .models import Student, Friendship1


# Create your views here.

image_bytes = create_graph()

def index(request):
    context_dict = { 'data' : image_bytes}
    return render(request, 'index.html', context_dict )


def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            student = data['student']
            friend1 = data['friend1']
            friend2 = data['friend2']
            friend3 = data['friend3']

            friendship1 = Friendship1( student = student, friend = friend1)
            friendship1.save()

            friendship2 = Friendship1( student = student, friend = friend2)
            friendship2.save()

            friendship3 = Friendship1( student = student, friend = friend3)
            friendship3.save()

            # ...

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('main_app:index'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()

    return render(request, 'forms.html', {'form': form})

def tables(request):
    context_tables = {'tables':create_table()}
    return render(request, 'tables.html',context = context_tables)