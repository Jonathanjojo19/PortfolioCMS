from django.shortcuts import render

def page_not_available_view(request):
    return render(request, 'not_available/notAvailable.html')