from bookstoremp import views
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("__debug__", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),
    path("api-token-auth/", obtain_auth_token, name="api-token-auth"),
    path("update_server/", views.update, name="update"),
    path("hello/", views.hello_world, name="hello_world"),
    path("", views.home, name="home"),  # Rota da home
]
