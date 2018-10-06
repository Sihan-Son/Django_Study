from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.BooksModelView.as_view(), name='index'),
    path('book/', views.BookList.as_visw(), name='book_list'),
    path('author/', views.AuthorList.as_view(), name='author_list'),
    path('publisher/', views.PubliserList.as_view(), name='publisher_list'),
    path('book/<int:pk>/', views.AutherDetail.as_view(), name='author_detail'),
    path('author/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]