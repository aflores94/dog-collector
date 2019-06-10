from django.shortcuts import render
from django.http import HttpResponse

class Dog:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

dogs = [
    Dog('Theo', 'goldendoodle', 'best boi', 3),
    Dog('Meow', 'pembroke welsh corgi', 'best butt around', 0),
    Dog('Goliath', 'dachsund', '3 legged dog', 4)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def dogs_index(request):
  return render(request, 'dogs/index.html', {'dogs': dogs})