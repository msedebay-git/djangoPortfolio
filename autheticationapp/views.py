from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from autheticationapp.forms import SignUpForm, EditUserProfileForm
from django.contrib import messages


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, "user creation successfully")
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def user_login(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            pwd = fm.cleaned_data['password']
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
        else:
            messages.info(request, "please enter the correct details")
    else:
        fm = AuthenticationForm()
    return render(request, 'login.html', {'form': fm})


def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditUserProfileForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'User profile has been updated')
        else:
            fm = EditUserProfileForm(instance=request.user)
        return render(request, 'profile.html', {'name': request.user, 'form': fm})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


# change password with old password
def user_change_password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'password changed successfully')
            return HttpResponseRedirect('/profile/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'changepassword.html', {'form': fm})


# change password without old password
def user_change_password1(request):
    if request.method == 'POST':
        fm = SetPasswordForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request, 'password changed successfully')
            return HttpResponseRedirect('/profile/')
    else:
        fm = SetPasswordForm(user=request.user)
    return render(request, 'changepassword1.html', {'form': fm})

#
#
# def sign_up(request):
#     if request.method == 'POST':
#         fm = SignUpForm(request.POST)
#         if fm.is_valid():
#             messages.success(request, 'User created successfully')
#             fm.save()
#             fm = SignUpForm()
#     else:
#         fm = SignUpForm()
#
#     return render(request, 'signup.html', {'form': fm})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         fm = AuthenticationForm(request, data=request.POST)  # Fix: Use request directly
#         if fm.is_valid():
#             uname = fm.cleaned_data['username']
#             pwd = fm.cleaned_data['password']
#             user = authenticate(username=uname, password=pwd)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/profile/')
#         else:
#             messages.info(request, 'Please enter the correct details')
#     else:
#         fm = AuthenticationForm()
#     return render(request, 'login.html', {'form': fm})
#
#
# def profile(request):
#     if request.user.is_authenticated:
#         return render(request, 'profile.html', {'name': request.user})
#     else:
#         return HttpResponseRedirect('/login/')
#
#
# def user_logout(request):
#     logout(request)
#     return HttpResponseRedirect('/login/')
#
#
# # change password with old password
# def user_change_password(request):
#     if request.method == 'POST':
#         fm = PasswordChangeForm(user=request.user, data=request.POST)
#         if fm.is_valid():
#             fm.save()
#             update_session_auth_hash(request, fm.user)
#             messages.success(request, 'password changed successfully')
#             return HttpResponseRedirect('/profile/')
#     else:
#         fm = PasswordChangeForm(user=request.user)
#     return render(request, 'changepassword.html', {'form': fm})
#
#
# # change password without old password
# def user_change_password1(request):
#     if request.method == 'POST':
#         fm = SetPasswordForm(user=request.user, data=request.POST)
#         if fm.is_valid():
#             fm.save()
#             update_session_auth_hash(request, fm.user)
#             messages.success(request, 'password changed successfully')
#             return HttpResponseRedirect('/profile/')
#     else:
#         fm = SetPasswordForm(user=request.user)
#     return render(request, 'changepassword1.html', {'form': fm})
