from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('about/', views.About, name='about'),    
    path('image-list/', views.ImageListView, name='image_list'),
    path('image-upload/', views.UploadImage, name='image_upload'),
    path('image-details/<int:image_id>/', views.ImageDetailView, name='image_details'),
    path('image-edit/<int:image_id>/', views.EditImage, name='image_edit'),
    path('image-remove/<int:image_id>/', views.ImageRemoveView, name='image_remove'),

    # category 
    path('category-add/', views.AddCategoryView, name='category_add'),

    path('', views.HomePage, name='home'),
    # path('<str:name>/', views.HomePage),
    # path('search/<str:search_query>/', views.HomePage),

]