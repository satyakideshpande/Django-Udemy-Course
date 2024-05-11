from django.shortcuts import render
from django.http.response import HttpResponse,Http404,HttpResponseNotFound,HttpResponseRedirect


# Create your views here.

def example_view(request):
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var = {'first_name':'Satyaki', 'last_name':'Deshpande', 'some_list': [1,2,3]}
    return render(request,'my_app/variables.html', context= my_var)
