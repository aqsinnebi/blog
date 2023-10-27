from django.urls import path

from . import views

urlpatterns = [
    
    
    
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('category/<int:id>',views.category,name='category'),
    path('blog-post/<int:id>',views.blog_post,name='blog-post'),
    path('send__mail/',views.send__mail,name='send__mail'),
    path('search/',views.search, name='search'),

    
]