from django.urls import path
from .views import index, add_forum, liatforum

urlpatterns = [
    path('', index, name='index'),
    path('add-forum/', add_forum, name='add_forum'),
]