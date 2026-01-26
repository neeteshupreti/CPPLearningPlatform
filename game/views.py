from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def game_view(request):
    return render(request, 'game/game.html')

@login_required
def update_xp(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        score = data.get('score', 0)
        request.user.learning_profile.xp += score
        request.user.learning_profile.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
