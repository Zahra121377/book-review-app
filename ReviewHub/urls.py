from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "add_review/<int:book_id>/",
        views.CreateReviewView.as_view(),
        name="add_review",
    ),
    path(
        "book_detail/<int:pk>/",
        views.BookDetailView.as_view(),
        name="book_detail",
    ),
    path("book_list", views.BookListView.as_view(), name="book_list"),
]
