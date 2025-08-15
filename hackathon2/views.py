from django.shortcuts import render
from .models import game_scores  # or GameScore, use your actual model name


# Create your views here.


def home(request):
    high_score_obj = game_scores.objects.order_by('-score').first()
    high_score = high_score_obj.score if high_score_obj else 0
    return render(request, 'hackathon2/snake.html', {'high_score': high_score})
