# appEncuestas/urls.py
# version de Django 2.1

from django.urls import path
from django.views import generic
from . import views



app_name = 'espacioEncuestas'
"""
urlpatterns = [
    # ex: /appEncuestas/
    path('', views.index, name='index'),
    # ex: /appEncuestas/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /appEncuestas/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /appEncuestas/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]