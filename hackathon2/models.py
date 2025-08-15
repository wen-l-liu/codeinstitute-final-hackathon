from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class game_scores(models.Model):
    gamer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="gamer"
    )
    score = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-score"]
        verbose_name = 'Game Score'
        verbose_name_plural = 'Game Scores'

    def __str__(self):
        return f"{self.gamer} | scored {self.score}"
