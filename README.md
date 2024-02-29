# photo image project

I want to make an image gallery:

- show/upload and remove images
- I want to have catogories
- I want to categorize them and change categories later
- I want to add tags to them
- I want to make it persoanl for each user
- I want to make favorite list from images
- I want to let people to left comment
- I want to confirmed comments before publish them

## MVT

[django workflow](assets/0%20nTL9xRiU9H9am0XF-2839485435.png)

[django request and response](assets/django_channels_structure-3897060420.png)

### make the first page (V)

- make a simple url and see the html result
- why make an app and what is it?
- app structure
  - base url
  - urls.py file
  - app name
  - add to settings installed app
  - use urls and views to show a page

### make a HTML to show data (T)

add tags to it:

- image
- h1 to h6
- p and div
- a and button tag
- html head bodey footer

- How to use bootstrap, bulma, tailwind
  
### Model(M)

#### Object Oriented programing (OOP)

- class
- attribute
- methods

why we use model?

#### image:

- name:
- description
- date
- image_file
- created
- active

### git review

- git add / git commit -m
- git checkout
- git branch
- git branch -d


#### category:

- name and relationship

#### method in models

- class Meta
- the name method
- property method (@property)


## Admin app

- how to reach
- how to use
- set admin file

### view 

- use model in view
- define a form for model
- show the form in html -> done
  
- handle the form in view -> done

## make other views

- make a list view -> done
- url name and redirection  -> done

- make a details view for image -> done
- make an edit view -> done
- make view to add/edit category  -> done
- (git and github, push code on github)
- remove an image (soft and hard)

- like an image
- show like numbers

## work with views

- making filter for list view (by date, category)
- making sort key for list view (by date, category)
- making search function

## working with forms

- making dropdown list for date (validation for date and a bit about validation)
- grab data from get/post request (with form with cleaned data) search function
- making complicated query like (date rage, gte, lte, Q , join)

## use modules

- django crispy forms

## use template for

- how to extend templates
- how to include templates
- template tags : [built-in template tags](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
  - block
  - comment (2 type)
  - extends
  - for and for empty
  - if
  - boolean
  - include
  - url 
- filters
  - date
  - length
  - linebreaks / linebreaksbr
  - lower / upper
  - time
  - truncatechars / truncatewords
  - static
  

## Style the html

- write a css 
- use libraries(bootstrap)



## advanced

### User

- making account app
- authentication (login logout, reset password, )
- list of likers

### Git workflow

- add commit in any changes
- using branch
- 