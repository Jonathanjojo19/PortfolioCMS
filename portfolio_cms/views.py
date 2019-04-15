from django.shortcuts import render

def page_not_found_view(request):
    return render(request, "not_available/notFound.html", status=404) 


def server_error_view(request):
    return render(request, "not_available/serverError.html", status=500) 
