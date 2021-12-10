from django.db import models
from django.db.models.fields import related
from django.db.models.fields.files import ImageField
from django_quill.fields import QuillField
from django_quill.quill import Quill


KYRGYZ = 'KYRGYZ'
RUSSIAN = 'RUSSIAN'
ENGLISH = 'ENGLISH'
TURKISH = 'TURKISH'

LANGUAGE_CHOICES = [
    (KYRGYZ, 'КЫРГЫЗЧА'),
    (RUSSIAN, 'НА РУССКОМ'),
    (ENGLISH, 'IN ENGLISH'),
    (TURKISH, 'TÜRKÇE'),
]

class Category(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Название жанра")

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
    
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="Название книги")
    author = models.CharField(max_length=100, null=True, verbose_name="Автор")
    pdf_file = models.FileField(upload_to="media/")
    cover = models.ImageField(upload_to="images/")
    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        default=RUSSIAN,
    )

    year = models.IntegerField()
    discription = models.TextField (max_length=1000, verbose_name="Описание книги")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="book")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
    
    def __str__(self):
        return self.name


class News(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="Заголовок новости")
    img = models.ImageField(upload_to='img/')
    body = QuillField(verbose_name = "Тело новости")
  

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
    
    def __str__(self):
        return self.name


class URL(models.Model):    
    name = models.CharField(max_length=200, null=True, verbose_name="Название")
    url_for = models.URLField(max_length = 250, verbose_name = 'Ссылка на YouTube')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="url")

    class Meta:
        verbose_name = "Url"
        verbose_name_plural = "Urls"
    
    def __str__(self):
        return self.name
   

class Authors(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name="Имя автора")
    body = QuillField(verbose_name = "Тело новости")
    create_at = models.DateTimeField(auto_now_add=True)
    short_description = models.TextField(max_length=200)
    description = models.TextField()


    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Биография автора"
    
    def __str__(self):
        return self.name

