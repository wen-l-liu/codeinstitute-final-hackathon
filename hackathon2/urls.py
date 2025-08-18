from django.urls import path, include
from .views import home
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('save-score', views.save_score, name='save_score'),
    path('delete-score/<int:score_id>/', views.delete_score, name='delete_score'),
    path('get-top-scores/', views.get_top_scores, name='get_top_scores'),
]