from django.urls import path

from blog.views import index, article

urlpatterns = [
    path('', index, name="index"),
    path('article-<str:numero>/', article, name="article"),

]