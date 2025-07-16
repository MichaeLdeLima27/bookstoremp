from django.contrib import admin
from django.urls import path, include
from bookstoremp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world, name='hello_world'),
    path('update_server/', views.update, name='update'),
    path('api-token-auth/', include('rest_framework.urls')),  # login/logout DRF browsable API
    path('api/products/', views.ProductListCreateAPIView.as_view(), name='api-product-list-create'),  # Listar e criar produtos
    path('api/products/<int:pk>/', views.ProductDetailAPIView.as_view(), name='api-product-detail'),  # Detalhe produto API
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Página HTML de produto
]
