# Create your views here.
from django.shortcuts import render

from ReviewHub.forms import ReviewForm

# class ReviewCreateView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     success_url = reverse_lazy("recipes:list")

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)


def add_review_view(request):
    context = {}
    context["form"] = ReviewForm()
    return render(request, "create_review.html", context)
