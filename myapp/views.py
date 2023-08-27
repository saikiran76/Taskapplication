from django.shortcuts import render
from django.http import HttpResponse

# create views
def helloworld(request):
    return HttpResponse("Hey there")

def home(request):
    return render(request, "task.html")