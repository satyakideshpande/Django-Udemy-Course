from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

#Creating a dictionary that stores all the routes

articles = {
    'sports': 'Sports View',
    'finance': 'Finance View',
    'politics': 'Political View'
}


def news_view(request,topic):
    return HttpResponse(articles[topic])

# View that adds two numbers
def add_view(request, num1, num2):
    result =  num1 + num2
    return HttpResponse(str(result))