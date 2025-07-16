from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import git

from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from product.models.product import Product
from product.serializers.product_serializer import ProductSerializer



@csrf_exempt
@api_view(['POST'])
def update(request):
    repo = git.Repo('/home/Michaelmp/bookstoremp')
    origin = repo.remotes.origin
    origin.pull()
    return Response({"detail": "Updated code on PythonAnywhere"}, status=status.HTTP_200_OK)


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


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
