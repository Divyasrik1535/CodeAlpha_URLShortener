from django.urls import path
from . import views

urlpatterns = [
    path('api/shorten/', views.shorten_url, name='shorten_url'),
    path('api/urls/', views.url_list, name='url_list'),
    path('s/<str:short_code>/', views.redirect_url, name='redirect_url'),
]