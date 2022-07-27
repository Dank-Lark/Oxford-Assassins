from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from account.forms import PayMembershipForm, RegisterUserForm, UpdateUserForm, CreateAssassinForm, UpdateAssassinForm, ChangePasswordForm
from account.models import Assassin, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Account Views:
#   account
#   loginForm
#   logoutForm
#   registerForm
#   profile

def alertErrors(request, form_errors):
    errors = str(
        " ".join(
            map(
                lambda s: s[4:], 
                filter(
                    lambda s: s.startswith("  * "), 
                    form_errors.as_text().split("\n")
                )
            )
        )
    )
    messages.error(request, errors)

####################################################################################################


@login_required(login_url='login')
def account(request):
    form_user = UpdateUserForm(instance=request.user)
    form_password = ChangePasswordForm(request.user)

    assassin = request.user.assassin
    if not request.user.paid: 
        form_assassin = PayMembershipForm()
        action_assassin = "pay_membership/"
        value_assassin = "Pay Membership"
    elif assassin is None:
        form_assassin = CreateAssassinForm()
        action_assassin = "create_assassin/"
        value_assassin = "Create Assassin"
    else:
        form_assassin = UpdateAssassinForm(instance=assassin)
        action_assassin = "update_assassin/"
        value_assassin = "Update Assassin"
   
    context = {
        'form_user': form_user, 
        'form_password': form_password,
        'form_assassin': form_assassin,
        'action_assassin': action_assassin,
        'value_assassin': value_assassin,
    }
    return render(request, 'account/account.html', context)


####################################################################################################


@login_required(login_url='login')
def updateUser(request):
    if request.method != 'POST':
        return redirect('account')

    form = UpdateUserForm(request.POST, instance=request.user)

    if form.is_valid():
        user = form.save(commit=False) 
        user.username = user.username.lower()
        user.email = user.email.lower()
        user.save()
    else:
        alertErrors(request, form.errors)

    return redirect('account')


    
####################################################################################################


@login_required(login_url='login')
def changePassword(request):
    if request.method != 'POST':
        return redirect('account')

    form = ChangePasswordForm(request.user, request.POST)

    if form.is_valid():
        form.save()
    else:
        alertErrors(request, form.errors)

    return redirect('account')


####################################################################################################


@login_required(login_url='login')
def createAssassin(request):
    if (request.method != 'POST'):
        return redirect('account')

    form = CreateAssassinForm(request.POST)
    if form.is_valid():
        form.save() 
        user = request.user
        user.assassin = form.instance
        user.save()
    else:
        alertErrors(request, form.errors)
        
    return redirect('account')
    


####################################################################################################


@login_required(login_url='login')
def updateAssassin(request):
    if (request.method != 'POST'):
        return redirect('account')

    form = UpdateAssassinForm(request.POST, instance=request.user.assassin)
    if form.is_valid():
        form.save()
    else:
        alertErrors(request, form.errors)

    return redirect('account')


####################################################################################################


@login_required(login_url='login')
def payMembership(request):
    if (request.method != 'POST'):
        return redirect('account')

    form = PayMembershipForm(request.POST)
    if form.is_valid():
        user = request.user
        user.request_pay = True
        user.save()
    else:
        alertErrors(request, form.errors)

    return redirect('account')


####################################################################################################


def loginForm(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            pass

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') #ToDo - ?next=/.../ parameters are not handled

    context = { 'page': 'login' }
    return render(request, 'account/loginregister.html', context)


####################################################################################################


def registerForm(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            alertErrors(request, form.errors)

    context = { 
        'page': 'register', 
        'form': form,
    }
    return render(request, 'account/loginregister.html', context)


####################################################################################################


def logoutForm(request):
    logout(request)
    return redirect('home')


####################################################################################################


@login_required(login_url='login')
def profile(request):
    context = {}
    return render(request, 'account/profile.html', context)
