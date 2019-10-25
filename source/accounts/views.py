from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import resolve

redirect_url = ''

def login_view(request):
    context = {}
    global redirect_url
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(redirect_url)
        else:
            context['has_error'] = True

    if request.method == 'GET':
        redirect_url = request.GET.get('next')
        return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:main_url')
