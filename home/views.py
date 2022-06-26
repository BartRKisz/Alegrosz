from django.shortcuts import render

def home_view(request):
    name = "Alegrosz"
    return render(request, 'home/home.html', {"name": name})