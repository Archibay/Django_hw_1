from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    path('triangle/', views.triangle, name='triangle'),
    path('person/', views.person_create, name='person_create'),
    path('person/<int:pk>/', views.person_update, name='person_update'),
]
