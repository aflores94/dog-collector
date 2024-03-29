from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from .models import Dog, Toy

class DogCreate(CreateView):
  model = Dog 
  fields = '__all__'

class DogUpdate(UpdateView): 
  model = Dog 
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog 
  success_url = '/dogs/'

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')


def dogs_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', {'dogs': dogs})

def dogs_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  feeding_form = FeedingForm()
  return render(request, 'dogs/detail.html', {
    'dog': dog, 'feeding_form': feeding_form
  })

def add_feeding(request, dog_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.dog_id = dog_id
    new_feeding.save()
  return redirect('detail', dog_id=dog_id)


class ToyList(ListView):
  model = Toy


class ToyDetail(DetailView):
  model = Toy


class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'


class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']


class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'
