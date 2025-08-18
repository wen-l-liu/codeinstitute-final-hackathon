# For deleting scores
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
# ...existing code...

@login_required
def delete_score(request, score_id):
    score = get_object_or_404(game_scores, id=score_id)
    if score.gamer == request.user:
        score.delete()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'error'}, status=403)
    return redirect('home')
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
        {
            'id': score.id,
            'username': score.gamer.username,
            'score': score.score,
            'is_owner': request.user.is_authenticated and score.gamer == request.user
        }
        for score in top_scores
    ]
    return JsonResponse({'top_scores': scores_data})
