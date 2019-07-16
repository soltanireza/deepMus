from django.contrib import admin
from django.urls import path
from app.views import index, predict, predicted, about, question, samples

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('predict/', predict, name='predict'),
    path('predicted/', predicted, name='predicted'),
    path('samples/', samples, name='samples'),
    path('question/', question, name='question'),
]
