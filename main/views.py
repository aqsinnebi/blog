from django.shortcuts import render,redirect
from . models import Test , Comment
from django.views.generic import DetailView,ListView,DeleteView
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.mail import send_mail
from django.contrib import messages



# Create your views here.

def index(request):
    data = Test.objects.raw(" SELECT * FROM main_test GROUP BY category")
    

    
    say = Test.objects.all()
    say1 = Test.objects.filter(category="Golang").count()

    content = Test.objects.filter(category = "Golang").all()

    test = Test.objects.all().order_by('-id')
    
    # test = Test.objects.values_list("category","metn")

    # test1 = Test.objects.all().values()

    context = {
        
        'data':data,
        'say1':say1,
        'say':say,
        'content': content,
        'test':test,
        
      
        
    }
    
    return render(request,"main/index.html",context)


def about(request):
    return render(request,'main/about.html')



def contact(request):
    
    
    return render(request,'main/contact.html')

def category(request,id):
    
    data = Test.objects.get(id = id)
    
    a = data.category
    
    test = Test.objects.filter(category = a)
    
    return render(request,'main/category.html',{'test':test})



def blog_post(request,id):
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        comment_id = request.POST['comment_id']
        test = Comment(name=name, email=email, message=message,comment_id=comment_id)
        test.save()
        
        
    comments = Comment.objects.filter(comment_id = id)

    
    
    data = Test.objects.filter(id=id)
    return render(request,'main/blog-post.html',{'data':data,'comments':comments,'id':id})


def send__mail(request):   
    
    subject = request.POST['subject'] , request.POST['email']
    message = request.POST['text']
    
    email_from = request.user.email
    recipient_list =[ "aqsinnebizade222@gmail.com" ]

    send_mail( subject, message, email_from, recipient_list )
    
    return redirect('contact')



def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        sc = Test.objects.filter(category__contains=search)
    
    context = {
        
        'sc':sc
        
    }
    return render(request, 'main/search.html', context)




