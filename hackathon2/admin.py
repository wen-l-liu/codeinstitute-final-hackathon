from django.contrib import admin
from .models import game_scores

# Register your models here.

@admin.register(game_scores)
class GameScoresAdmin(admin.ModelAdmin):
    list_display = ('gamer', 'score', 'created_on')
    list_filter = ('gamer',)
    search_fields = ('gamer__username',)
    
