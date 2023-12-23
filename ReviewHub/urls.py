from django.urls import path

from . import views

urlpatterns = [
    path("add_review", views.add_review_view, name="add_review"),
    path("book_list", views.BookListView.as_view(), name="book_list"),
]
