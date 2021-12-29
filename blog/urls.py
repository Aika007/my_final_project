from django.urls import path
from .views import index, news_detail, authors_detail, books_list, open_pdf, news_list, authors_list, category_detail, books_detail, open_pdf
app_name = 'blog'



urlpatterns = [
    path('', index, name = "index"),
    path('news/<int:pk>/', news_detail, name = "news_detail" ),
    path('authors/', authors_list, name = 'authors_list'),
    path('authors_detail/<int:pk>/', authors_detail, name = "authors_detail" ),
    path('books/', books_list, name = 'books_list'),
    path('books_detail/<int:pk>/', books_detail, name = "books_detail" ),
    path('books_detail/pdf/<int:pk>/', open_pdf, name = "pdf" ),
    path('category_detail/<int:pk>/', category_detail, name = "category_detail" ),
    path('news/', news_list, name = 'news_list'),

]
