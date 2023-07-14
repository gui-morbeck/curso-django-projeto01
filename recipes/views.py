from django.shortcuts import render

def view_home(request):
    return render(request, 'recipes/home.html', context=
                  {'name': 'Gui'})

def view_about(request):
    return render(request, 'recipes/about.html', status=200)

def view_contact(request):
    return render(request, 'recipes/contact.html')