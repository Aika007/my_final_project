from django.shortcuts import render
from blog.models import News, Book, Category, URL, Authors
from bs4 import BeautifulSoup as BSHTML


def index(request):
    news = News.objects.all()
    authors = Authors.objects.all()
    return render(request,'index.html', context={"news":news,"authors":authors})

def news_list(request):
    news = News.objects.all()
    if request.method=="POST":
        searched=request.POST['searched']
        news=News.objects.filter(name__contains=searched)
        return render(request,'news.html', context={"news":news})

    return render(request, 'news.html', context={"news": news})

def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    return render(request, 'news_detail.html', context = {'news':news})


def books_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    if request.method=="POST":
        searched=request.POST['searched']
        books=Book.objects.filter(name__contains=searched)
        return render(request,'books.html', context={"books":books,"categories":categories})
  
    return render(request,'books.html', context={"books":books,"categories":categories})


def category_detail(request,pk):
    books = Book.objects.filter(category__id=pk)
    print(books)
    categories = Category.objects.all()
    return render(request,'books.html', context={"books":books,"categories":categories})


def books_detail(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'books_detail.html', context = {'book':book})

# def categories(request):
#     categories = Categories.objects.all()
#     # return render(request, 'books_detail.html', context={
#     #     "Мировая литература", "Кыргыз адабияты", "Türk edebiyatı", "Русская литература", "Поэзия"
#     #     })

def authors_list(request):
    author = Authors.objects.all()
    if request.method=="POST":
        searched=request.POST['searched']
        author=Authors.objects.filter(name__contains=searched)
        return render(request,'authors.html', context={"authors":author})

    return render(request,'authors.html', context={"authors":author})

def authors_detail(request, pk):
    author = Authors.objects.get(pk=pk)
    return render(request, 'authors_detail.html', context = {'author':author})

