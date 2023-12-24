from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_review", views.add_review_view, name="add_review"),
    path("book_list", views.BookListView.as_view(), name="book_list"),
]
