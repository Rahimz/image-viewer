from django.shortcuts import render, redirect

from django.http import HttpResponse
import datetime
from django.utils import timezone
import random
from django.db.models import Q

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


def ImageListView(request, category_name=None, sort_field=None):
    images = Image.objects.filter(active=True)
    filter = None 

    if category_name:
        category_obj = Category.objects.get(name=category_name)
        images = images.filter(category=category_obj)
        filter = category_name

    if sort_field:
        images = images.order_by(sort_field)
        
    search_query = None
    if request.GET.get('search'):
        search_query = request.GET.get('search')

        images = Image.objects.filter(active=True).filter(
            Q(name__icontains=search_query) | Q(category__name__icontains=search_query) | Q(description__icontains=search_query) 
            )

    context = {
        'images': images,
        'filter': filter,
        'sort_field': sort_field,
        'query': search_query 
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
            'image': image_from_database 
        }
    )

def ImageRemoveView(request, image_id):
    image_obj = Image.objects.get(id=image_id)

    # image_obj.delete()
    image_obj.active = False
    image_obj.save()

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

def ImageLikeView(request, image_id):
    image = Image.objects.get(id=image_id)
    image.like_counts += 1 
    image.save()
    return redirect('viewer:image_details', image.id)