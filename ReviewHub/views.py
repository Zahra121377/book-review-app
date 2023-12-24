# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

from ReviewHub.forms import ReviewForm
from ReviewHub.models import Book

# class ReviewCreateView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     success_url = reverse_lazy("recipes:list")

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


def index(request):
    return render(request, "ReviewHub/index.html")


def add_review_view(request):
    context = {}
    context["form"] = ReviewForm()
    return render(request, "ReviewHub/add_review.html", context)


class BookListView(ListView):
    model = Book
    context_object_name = "books"
