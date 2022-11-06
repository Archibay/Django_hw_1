import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    city_name = models.CharField(max_length=200, unique=True)
    city_index = models.IntegerField(unique=True)

    def __str__(self):
        return self.city_name


class Article(models.Model):
    article_name = models.CharField(max_length=200)
    article_desc = models.TextField(max_length=1000, )

    def __str__(self):
        return self.article_name


class Client(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.CharField(max_length=200)
    client_phone = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    article = models.ManyToManyField(Article)

    def __str__(self):
        return self.client_name


class Shipper(models.Model):
    sipper_name = models.CharField(max_length=200)
    city = models.OneToOneField(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.sipper_name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.last_name


class Logs(models.Model):
    class Method(models.TextChoices):
        GET = 'GE', _('Get request')
        HEAD = 'HE', _('Head request')
        POST = 'PO', _('Post request')
        PUT = 'PU', _('Put request')
        DELETE = 'DE', _('Delete request')
        CONNECT = 'CO', _('Connect request')
        OPTIONS = 'OP', _('Options request')
        TRACE = 'TR', _('Trace request')
        PATCH = 'PA', _('Path request')

    path = models.CharField(max_length=100)
    method = models.CharField(max_length=2, choices=Method.choices)
    timestamp = models.DateTimeField(datetime.datetime.now())
    values = models.JSONField()

    def __str__(self):
        return self.path
