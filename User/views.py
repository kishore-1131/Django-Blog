from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm, UserUpdateForm, UserInfoUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm,AuthenticationForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def RegisterView(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            form.save()
            return redirect('login')
    
    else:
        form = RegistrationForm()
    args = {'form':form}
    return render(request, 'User/register.html', args) 
@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserInfoUpdate(request.POST,request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account is Updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm( instance = request.user)
        p_form = UserInfoUpdate(instance = request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'User/profile.html', context )


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user= request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(user = request.POST)
    args = {'form':form}
    return render(request,'User/change_password.html', args)
