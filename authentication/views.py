from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def login_view(request):
    response = {}
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_superuser or request.user.is_staff:
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                return redirect("portfolio:index")
            else:
                logout(request)
        return redirect(request.POST.get("next"))
    return render(request, "authentication/auth.html", {
        "form" : AuthenticationForm(),
        "feedback" : ""
    })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("portfolio:index")
    return redirect(request, "portfolio:index")
