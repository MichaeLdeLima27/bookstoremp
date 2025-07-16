from django.contrib import admin
from django.urls import path, include
from bookstoremp import views
from bookstoremp.views import ProductDetailAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('hello/', views.hello_world, name='hello_world'),
    path('update_server/', views.update, name='update'),
    path('api-token-auth/', include('rest_framework.urls')),
    path('api/product/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),  # API REST para detalhes do produto
    path('product/<int:pk>/', views.product_detail, name='product_detail'),  # Página de detalhes do produto (HTML)
]
