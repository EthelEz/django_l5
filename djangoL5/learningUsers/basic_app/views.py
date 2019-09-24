from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm, UserForm
# In creating views for login, we'd be using a lot of django functionality, hence would be imported
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# (1) homepage which is the index view
def index(request):
    return render(request, 'basic_app/index.html')


# (2) views for the registration, which connected in urls' view.register
def register(request):

    registered = False              #This tells us if someone is registered or not

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)    #this would essentially set the hashing pwd
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user                 #This sets the OneToOne relationship

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']               # NB: even if this is a csv, we're supposed to be linking them up wi request.FILES as shown

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered})
# This is a login view
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')       #this is to get data from the username in login.html
        password = request.POST.get('password')         #same as above.

        user = authenticate(username=username, password=password)        #this would authenticate the user for you

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))      #if the user is authentiated, grab the user request and redirect them to homepage.
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Someone tried to login and failed!")
            print("Username : {} and password {}".format(username, password))
            return HttpResponse("Invalid Login details supplied!")
    else:
        return render(request, 'basic_app/login.html', {})


@login_required
def special(request):
    return HttpResponse('You are logged in, Nice!')
# logout view
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
