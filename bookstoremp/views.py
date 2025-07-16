from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Product

import git

@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo('/home/Michaelmp/bookstoremp')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {'product': product}
    return HttpResponse(template.render(context, request))
