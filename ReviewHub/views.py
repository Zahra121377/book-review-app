# Create your views here.
from django.shortcuts import redirect, render
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


def add_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.save()
            return redirect("book_detail", book_id=book_id)
    else:
        form = ReviewForm()

    return render(request, "ReviewHub/add_review.html", {"form": form})


class BookListView(ListView):
    model = Book
    context_object_name = "books"
