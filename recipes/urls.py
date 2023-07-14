from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', view_home),
    path('about/', view_about),
    path('contact/', view_contact)
]