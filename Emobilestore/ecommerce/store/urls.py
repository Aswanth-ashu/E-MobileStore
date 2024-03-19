from django.contrib import admin
from django.urls import path
from.import views
from django.urls import path
from store import views
from .models import APIKey


urlpatterns = [
    path('', views.index, name="home"),
    path('collections',views.collections, name="collections"),
    path('login',views.loginn, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout,name="logout"),
    path('collections/<str:slug>',views.collectionsview,name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>',views.productview,name="productview"),
    path('contact',views.coustmerdet,name='coustmerdet'),
    path('payment',views.payment,name='payment'),
    path('api/keys/', views.APIKeyListCreateView.as_view(), name='api-key-list-create'),
    path('api/keys/<int:pk>/', views.APIKeyRetrieveUpdateDestroyView.as_view(), name='api-key-detail'),
  
  
     
     
 
]



