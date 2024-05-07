from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseNotFound

# Create your views here.

#Creating a dictionary that stores all the routes

articles = {
    'sports': 'Sports View',
    'finance': 'Finance View',
    'politics': 'Political View'
}


def news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        #return Http404("404 Generic Response")
        result = 'Page not found'
        return HttpResponseNotFound(result)

# View that adds two numbers from UI
def add_view(request, num1, num2):
    result =  num1 + num2
    return HttpResponse(str(result))