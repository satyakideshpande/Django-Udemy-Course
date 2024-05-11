from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect


# Create your views here.

def example_view(request):
    return render(request,'my_app/example.html')
