from django.shortcuts import render, redirect

from django.http import HttpResponse
import datetime
from django.utils import timezone
import random

from viewer.models import Image, Category
from .forms import ImageForm, CategoryForm

def HomePage(request):
    now = datetime.datetime.now()
    now_tz = timezone.now()

    l = ['شنبه' , 'یک شنبه ' , 'دو شنبه' , 'سه شنبه']

    r = random.choice(l)
    x = random.randint(1, 12000)

    images = Image.objects.all().order_by('id')


    

    return render(
        request,
        'home/home.html',
        {
            'html_date_time': now,
            'time_tz': now_tz,
            'r': r,
            'images_of_albums': images,
           
        }
    )

def About(request):
    return render(
        request,
        'home/about_us.html'
    )


def ImageListView(request):
    images = Image.objects.all()

    context = {
        'images': images
    }

    return render(
        request,
        'home/image_list.html',
        context

    )

def UploadImage(request):
    if request.method == 'POST':
        print(request.POST)    
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            # form.shoot_date = lkdjhfgl
            form.save()
            
            return redirect ('viewer:image_list') #('app_name:url_name') 

    else:    
        form = ImageForm()

    return render(
        request,
        'home/image_upload.html',
        {
            'form': form
        }
    )

def EditImage(request, image_id):
    image_obj = Image.objects.get(id=image_id)

    if request.method == 'POST':
        # print(request.POST)    
        form = ImageForm(data=request.POST, files=request.FILES, instance=image_obj)
        if form.is_valid():
            # form.shoot_date = lkdjhfgl
            form.save()
            
            return redirect ('viewer:image_list') #('app_name:url_name') 

    else:    
        form = ImageForm(instance=image_obj)

    return render(
        request,
        'home/image_upload.html',
        {
            'form': form
        }
    )


def ImageDetailView(request, image_id):
    image_from_database = Image.objects.get(id=image_id)
    return render (
        request,
        'home/image_detials.html',
        {
            'image_html_object_name': image_from_database 
        }
    )

def ImageRemoveView(request, image_id):
    image_obj = Image.objects.get(id=image_id)

    image_obj.delete()

    return redirect ('viewer:image_list')


def AddCategoryView(request):
    if request.method== 'POST':
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)

            if Category.objects.filter(name__iexact=new_category.name).exists():

                print('The category exists')
                return redirect('viewer:category_add')
            new_category.save()
            # email to admin 
            # Object for notification 
            # add a record for activity log
            


            return redirect ('viewer:home')

    else:
        form = CategoryForm()
    return render (
        request, 
        'home/image_upload.html',
        {
            'form': form,
        }
    )