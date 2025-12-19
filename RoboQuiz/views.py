import json
from django.shortcuts import render
from game.models import Question

def game_home(request):
    # Fetch all questions from the DB
    db_questions = Question.objects.prefetch_related('options').order_by('order')
    
    game_levels = []
    for q in db_questions:
        options_list = list(q.options.all())
        
        # Find the index of the correct answer
        correct_idx = 0
        for i, opt in enumerate(options_list):
            if opt.is_correct:
                correct_idx = i
        
        game_levels.append({
            "story": q.story,
            "code": q.code,
            "options": [opt.text for opt in options_list],
            "correct": correct_idx,
            "hint": q.hint
        })

    # If the database is empty, provide a default level so the JS doesn't break
    if not game_levels:
        game_levels = [{
            "story": "No missions found. Please add some in the Admin panel!",
            "code": "// Add questions at /admin",
            "options": ["Understood"],
            "correct": 0,
            "hint": "Go to 127.0.0.1:8000/admin"
        }]

    return render(request, 'index.html', {
        'levels_json': json.dumps(game_levels)
    })