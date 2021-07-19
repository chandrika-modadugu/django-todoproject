from django.shortcuts import render,redirect,reverse
from todoapp.forms import TaskForm,UserForm
from todoapp.models import Task,User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request,'todoapp/index.html')

@login_required
def home(request):
    return render(request,'todoapp/index.html')
    #return render(request,'todoapp/home.html')


@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def AddTask(request,username):
    model = User
    userdtls=User.objects.get(username=username)
    #model=Task
    #t=Task.objects.filter(user=userdtls.id)
    name = User.objects.get(id=userdtls.id)
    form=TaskForm()
    if request.method=="POST":
        #    formname=Task(user=name)
        form=TaskForm(request.POST)
        if form.is_valid():
            my_form=form.save(commit=False)
            my_form.user=name
            my_form.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request,'todoapp/addtask.html',{'task_form':form})

def ViewTask(request,username):
    model = User
    userdtls=User.objects.get(username=username)
    print("userid{}".format(userdtls.id))
    model=Task
    tasks=Task.objects.filter(user=userdtls.id)
    return render(request,'todoapp/viewtask.html',{'tasks':tasks})

def edittask(request,username,Title):
    model = User
    userdtls=User.objects.get(username=username)
    model=Task
    task=Task.objects.filter(user=userdtls.id,Title=Title).first()

    form=TaskForm(instance=task)
    if request.method=="POST":
        if 'edit' in request.POST:
            form=TaskForm(request.POST,instance=task)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('index'))

        if 'delete' in request.POST:
            task.delete()
            return HttpResponseRedirect(reverse('index'))

    return render(request,'todoapp/edittask.html',{'edit_Task':form})

def deletetask(request,username,Title):
    model = User
    userdtls=User.objects.get(username=username)
    model=Task
    task=Task.objects.filter(user=userdtls.id,Title=Title).first()
    task.delete()
    return HttpResponseRedirect(reverse('index'))

#    return render(request,'todoapp/home.html')


def register(request):
    registered = False
    user_form=UserForm
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    return render(request,'todoapp/registration.html',{'user_form':UserForm,'registered':registered})



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
                return HttpResponseRedirect(reverse('index'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'todoapp/login.html',{})
