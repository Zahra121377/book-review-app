from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    context = forms.CharField(
        required=True,
        label="Review",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Write your review here",
            }
        ),
    )
    rating = forms.ChoiceField(
        choices=Review.STARS,
        label="Rating",
        widget=forms.RadioSelect,
    )
    name = forms.CharField(
        required=False,
        label="User Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter recipe name"}
        ),
    )

    class Meta:
        model = Review
        fields = ["context", "rating", "name"]
