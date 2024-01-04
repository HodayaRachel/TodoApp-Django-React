from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
import pymongo
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")


client = pymongo.MongoClient("****")

# db = client.test


# Define Db Name
dbname = client['TodoApp']

# Define Collection
collection = dbname['Todos']

task_1 = {
    "title": "Sammy",
    "description": "Shark",
    "completed": True

}

collection.insert_one(task_1)

task_details = collection.find({})

for r in task_details:
    print(r['title'])


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))
