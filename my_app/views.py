from django.shortcuts import render,redirect
from django.http import HttpResponse
#render package- correctly display views when passing templates
# Create your views here.

#def index(request):  

    #return HttpResponse("welcome to web development")

# to make this work need to configure my_app > urls


#def home(request):
    #return HttpResponse("home page")


    #USING HTML PAGE
    # create html page inside templates


##def index(request):  

    #return render(request,'index.html')


#def home(request):  

    #return render(request,'home.html')

# configure settings templates DIR


from .models import book

def createbook(request):
    books=book.objects.all()
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')

        books=book(title=title,author=author,price=price)
        books.save()

    return render(request,'book.html',{'book':books})

def listbook(request):
    books=book.objects.all()

    return render(request,'listbook.html',{'books':books})

def detailsview(request,book_id):
    books=book.objects.get(id=book_id)
    return render(request,'detailsview.html',{'bookss':books})

def updateview(request,book_id):
    books= book.objects.get(id=book_id)
    if request.method=="POST":
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=request.POST.get('price')

        books.title=title
        books.author=author
        books.price=price
        books.save()
        # return redirect('/')

    return render(request,'updateview.html',{'bookss':books})
# deleteview crud 4
