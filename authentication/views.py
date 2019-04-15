from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def default_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser or request.user.is_staff:
                return redirect("portfolio:index")
            else:
                logout(request)
        return render(request, "authentication/auth.html", {
            "form" : AuthenticationForm(),
            "feedback" : "Sorry, you are not authorized to edit the page",
            "next" : reverse('authentication:def_login')
        })
    return render(request, "authentication/auth.html", {
        "form" : AuthenticationForm(),
        "feedback" : "",
        "next" : reverse('authentication:def_login')
    })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser or request.user.is_staff:
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                return redirect("cms:dashboard")
            else:
                logout(request)
        return render(request, "authentication/auth.html", {
            "form" : AuthenticationForm(),
            "feedback" : "Sorry, you are not authorized to edit the page",
            "next" : reverse('authentication:login')
        })
    return render(request, "authentication/auth.html", {
        "form" : AuthenticationForm(),
        "feedback" : "",
        "next" : reverse('authentication:login')
    })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("portfolio:index")
    return redirect(request, "portfolio:index")
