from django.db import models

from django.urls import reverse
import uuid
from django.template import defaultfilters

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def __str__(self):
        return self.name


class Language(models.Model):
    code = models.CharField(unique=True, max_length=2, help_text='Enter a Lenguage CODE like (EN or ES)')
    name = models.CharField(max_length=50, help_text='Enter the complete name for this language')

    def get_absolute_url(self):
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        return '({0}) {1}'.format(self.code, self.name)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter de brief description')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify('{0}-{1}'.format(self.title[:100], self.id))
        super(Book, self).save(*args, **kwargs)

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all() ])
    display_genre.short_description = 'Genre'

    def display_language(self):
        return ', '.join([ self.language.name ])

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this book')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.book.title)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    slug = models.SlugField(max_length=100, null=True)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify('{0}-{1}-{2}'.format(self.first_name, self.last_name, self.id))
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return '{0}, ({1})'.format(self.last_name, self.first_name)

