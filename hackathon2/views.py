from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'hackathon2/snake.html')
