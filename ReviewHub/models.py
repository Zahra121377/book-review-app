from math import floor

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg


def validate_username(value):
    if len(value) < 3 or len(value) > 20:
        raise ValidationError(
            ("Username should be between 3 and 20 characters."),
            code="invalid_username_length",
        )


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    about = models.TextField(max_length=500)
    author = models.CharField(max_length=70)
    pub_year = models.PositiveSmallIntegerField(blank=True, null=True)
    GENRE_LIST = [
        ("Fiction", "Fiction"),
        ("Novel", "Novel"),
        ("Narrative", "Narrative"),
        ("Mystery", "Mystery"),
        ("Sci-Fi", "Science Fiction"),
        ("Fantasy", "Fantasy"),
        ("Thriller", "Thriller"),
        ("History", "History"),
        ("Memoir", "Memoir"),
        ("Humor", "Humor"),
    ]
    genre = models.CharField(max_length=25, choices=GENRE_LIST)
    avg_rating = models.IntegerField(max_length=1)

    def __str__(self):
        return self.title

    def average_rating(self):
        self.avg_rating = (
            floor(self.review_set.aggregate(Avg("rating"))["rating__avg"]) or 0
        )


class User(models.Model):
    username = models.CharField(max_length=20, validators=[validate_username])
    email = models.EmailField()


class Review(models.Model):
    context = models.TextField(max_length=1000)
    STARS = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    rating = models.CharField(max_length=1, choices=STARS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_avg_rating()
