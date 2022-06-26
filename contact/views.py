from django.shortcuts import render

def contact_page(request):
    contact = "Contact"
    return render(request, 'contact/contact.html', {"contact": contact})