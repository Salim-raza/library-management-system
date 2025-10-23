from django.urls import path
from .views import *

urlpatterns = [
    path("book_add/", book_add, name="book_add"),
    path("book_update/<int:id>/", book_update, name="book_update"),
    path("delete/<int:book_id>/", delete_book, name="delete_book"),
    path("search_book/", search_book, name="search_book"),
    path("search_all_book/", search_all_book, name="search_all_book"),
    path("search/<str:title>/", search, name="search"),
]