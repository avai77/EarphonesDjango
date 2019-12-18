from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path
from django.conf.urls.static import static
from shop import views
from .views import *

app_name = "shop"

urlpatterns = [
                  path('', views.home, name="home"),
                  path('signup/', views.signup, name="signup"),
                  path('signin/', views.signin, name="signin"),
                  path('signout/', views.signout, name="signout"),
                  path('search/', views.search, name="search"),
                  path('<slug>/', views.detail, name="detail"),
                  path('categories/<slug>/', views.categories, name="categories"),
                  path('shop/product/add/', views.product_add, name='product_add'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
