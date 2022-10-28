from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=200)
    city_index = models.IntegerField(max_length=5, unique=True)

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
