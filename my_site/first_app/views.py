from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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

def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic =  topics_list[num_page]

    return HttpResponseRedirect(reverse('topic-page',args=[topic]))