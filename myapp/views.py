from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonForm

people = []

class Person:
    def __init__(self, username, password):
        self.username = username
        self.password = password

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            people.append(person)
            return HttpResponseRedirect('/')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form, 'people': people})

def show_people(request):
    return render(request, 'show_people.html', {'people': people})

