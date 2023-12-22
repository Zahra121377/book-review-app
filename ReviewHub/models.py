from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
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

    def __str__(self):
        return self.title


class Review(models.Model):
    context = models.TextField(max_length = 1000)
    STARS = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
    ]
    rating = models.CharField(max_length = 1, choices = STARS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)