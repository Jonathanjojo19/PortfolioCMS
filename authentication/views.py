from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            return redirect('portfolio:index')
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/auth.html', {'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('portfolio:index')
    return redirect(request, 'portfolio:index')
