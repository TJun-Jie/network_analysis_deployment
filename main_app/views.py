from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required

from .forms import InputForm, UserForm
from .generateGraph import create_graph
from .tables import create_table
from .models import Student, Friendship1
from .decorators import allowed_users
from django.contrib.auth.models import User


# Create your views here.

image_bytes = create_graph()

def index(request):
    return render(request, 'index.html')


@login_required
@allowed_users(allowed_roles=['admin'])
def graph(request):
    number_of_students = User.objects.filter(is_staff=False).count()
    number_of_friendship_links = Friendship1.objects.all().count()
    number_of_friends = {}
    most_popular_student = get_most_popular_student()
    print(most_popular_student)
    context_dict = { 'data' : image_bytes, 'number_of_students': number_of_students, 'number_of_friendship_links': number_of_friendship_links, "most_popular_student_name": most_popular_student.first_name + " " + most_popular_student.last_name}
    return render(request, 'graph.html', context_dict )


@login_required
def get_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student = request.user
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
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
        student = request.user
        friendships = Friendship1.objects.filter(student__id = student.id)
        if(len(friendships) > 0):
            dct = {
                "friend1": friendships[0].friend,
                "friend2": friendships[1].friend,
                "friend3": friendships[2].friend
            }
        else:
            dct = {}
        print(dct)
        form = InputForm(initial=dct)

    return render(request, 'forms.html', {'form': form})

@login_required
@allowed_users(allowed_roles=['admin'])
def tables(request):
    context_tables = {'tables':create_table()}
    return render(request, 'tables.html',context = context_tables)

def register(request):
    registered =False

    if request.method =="POST":
        user_form =UserForm(data=request.POST)

        if user_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'registration.html',
                            {'user_form':user_form,
                            'registered':registered})


def user_login(request):

    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('main_app:index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('main_app:index'))


def get_most_popular_student():
    friends = Friendship1.objects.all()
    number_of_friends = {}
    highest_id = 0
    highest_number = 0

    for entry in friends: 
        if((entry.student.id) not in number_of_friends):
            number_of_friends[entry.student.id] = 0

    for entry in friends:
            # print(number_of_friends)
            number_of_friends[entry.friend.id] += 1
    for key in number_of_friends:
        if(number_of_friends[key] > highest_number):
            highest_id = key
            highest_number = number_of_friends[key]
    return User.objects.get(pk=highest_id)

def unauthorised(request):
    return render(request, 'unauthorised.html' )