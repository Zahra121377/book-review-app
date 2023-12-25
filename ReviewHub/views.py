# Create your views here.


from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView
from django.views.generic.edit import FormView

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


# def add_review(request, book_id):
#     book = Book.objects.get(pk=book_id)
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.book = book
#             review.save()
#             return redirect("book_detail", book_id=book.id)
#     else:
#         form = ReviewForm()

#     return render(request, "ReviewHub/add_review.html", {"form": form})


class CreateReviewView(FormView):
    template_name = "ReviewHub/add_review.html"
    form_class = ReviewForm

    def form_valid(self, form):
        book = get_object_or_404(Book, id=self.kwargs["book_id"])
        review = form.save(commit=False)
        review.book = book
        review.user = self.request.user
        review.save()
        return redirect(
            "book_list"
        )  # Adjust the URL name based on your URL patterns

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["book"] = get_object_or_404(Book, id=self.kwargs["book_id"])
        return context


class BookListView(ListView):
    model = Book
    context_object_name = "books"
