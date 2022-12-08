from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from django.http import HttpResponse
import pymongo
# Create your views here.


class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()


def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")


client = pymongo.MongoClient("mongodb+srv://<user>:<password>@cluster0.aq0uddv.mongodb.net/?retryWrites=true&w=majority")
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

