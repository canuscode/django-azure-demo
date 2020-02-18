from django.shortcuts import render
from django.http import HttpResponse
from . models import Stories


def homepage(request):
    stories = Stories.objects.all()
    return render(request, 'stories/homepage.html', {'stories': stories})