from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle')
]
