from django.test import TestCase
from django.shortcuts import render
from django.http import HttpResponse
# Create your tests here.
def test(request):
     return HttpResponse("Hello world")
    