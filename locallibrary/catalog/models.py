from django.db import models
from django.urls import reverse  # Used in get_absolute_url() to get URL for specified ID
from django.db.models import UniqueConstraint  # Constrains fields to unique values
from django.db.models.functions import Lower  # Returns lower cased value of field

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a particular genre instance."""
        return reverse('genre-detail', args=[str(self.id)])

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message="Genre already exists (case insensitive match)"
            ),
        ]


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    summary = models.TextField()
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        """String for representing the Model object."""
        return f"{self.first_name} {self.last_name}"

class BookInstance(models.Model):
    """Model representing a specific copy of a book (e.g. that can be borrowed)."""
    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} ({self.imprint})"

class Language(models.Model):
    name = models.CharField(max_length=100, help_text="Enter the language of the book")

    def __str__(self):
        return self.name
