from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import game_scores  # or GameScore, use your actual model name
from django.core import serializers


# Create your views here.


def home(request):
    high_score_obj = game_scores.objects.order_by('-score').first()
    high_score = high_score_obj.score if high_score_obj else 0
    top_scores = game_scores.objects.order_by('-score')[:10]
    return render(request, 'hackathon2/snake.html', {
        'high_score': high_score,
        'top_scores': top_scores
    })


@csrf_exempt
def save_score(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        score = data.get('score', 0)
        if request.user.is_authenticated:
            gamer = request.user
            # Check for duplicate score
            if not game_scores.objects.filter(gamer=gamer, score=score).exists():
                game_scores.objects.create(gamer=gamer, score=score)
        else:
            # Handle anonymous users if needed
            pass
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)


def get_top_scores(request):
    top_scores = game_scores.objects.order_by('-score')[:10]
    scores_data = [
        {'username': score.gamer.username, 'score': score.score}
        for score in top_scores
    ]
    return JsonResponse({'top_scores': scores_data})
