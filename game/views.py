from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Option


@login_required(login_url='accounts:login')
def game_home(request):
    """Display all available missions/questions"""
    questions = Question.objects.all().order_by('order')
    context = {
        'questions': questions,
        'total_questions': questions.count(),
    }
    return render(request, 'game/home.html', context)


@login_required(login_url='accounts:login')
def quiz_view(request, question_id):
    """Display a specific quiz question"""
    question = get_object_or_404(Question, pk=question_id)
    options = question.options.all()
    
    context = {
        'question': question,
        'options': options,
    }
    return render(request, 'game/quiz.html', context)


@login_required(login_url='accounts:login')
def check_answer(request, question_id):
    """Check if the selected answer is correct"""
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        selected_option_id = request.POST.get('option')
        
        if not selected_option_id:
            return render(request, 'game/quiz.html', {
                'question': question,
                'options': question.options.all(),
                'error': 'Please select an option'
            })
        
        selected_option = get_object_or_404(Option, pk=selected_option_id)
        is_correct = selected_option.is_correct
        
        context = {
            'question': question,
            'selected_option': selected_option,
            'is_correct': is_correct,
            'hint': question.hint if not is_correct else None,
        }
        return render(request, 'game/result.html', context)
    
    return render(request, 'game/quiz.html', {'question': get_object_or_404(Question, pk=question_id)})


@login_required(login_url='accounts:login')
def leaderboard(request):
    """Display leaderboard"""
    context = {
        'users': [
            {'rank': 1, 'name': 'Alice Johnson', 'score': 5200, 'missions': 8},
            {'rank': 2, 'name': 'Bob Smith', 'score': 4850, 'missions': 7},
            {'rank': 3, 'name': 'Carol Davis', 'score': 4600, 'missions': 6},
            {'rank': 4, 'name': 'David Wilson', 'score': 4200, 'missions': 6},
            {'rank': 5, 'name': 'Eve Martinez', 'score': 3900, 'missions': 5},
            {'rank': 6, 'name': request.user.first_name or request.user.username, 'score': 3500, 'missions': 5},
        ]
    }
    return render(request, 'game/leaderboard.html', context)

