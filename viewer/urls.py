from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('about/', views.About),
    path('', views.HomePage),
    # path('<str:name>/', views.HomePage),
    # path('search/<str:search_query>/', views.HomePage),

]
