from django.db import models
from django.db.models import Avg
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    about = models.TextField(max_length=500, default="Explain about book here")
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
    avg_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def update_average_rating(self):
        self.avg_rating = round(
            self.review_set.aggregate(Avg("rating"))["rating__avg"] or 0
        )
        self.save()


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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.CharField(max_length=20, default="Anonymous")
    pub_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_average_rating()
