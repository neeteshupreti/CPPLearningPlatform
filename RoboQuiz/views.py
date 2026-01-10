import json
from django.shortcuts import render
from game.models import Question

def game_home(request):
    # 1. Define your 5-6 DEFAULT questions
    game_levels = [
        {
            "story": "Robo-X fails to greet humans. Repair the speech module.",
            "code": 'int main() {\n  cout << "Hello World\n  return 0;\n}',
            "options": [ "Remove return","Add closing quotation mark", "Change int to float"],
            "correct": 1,
            "hint": "Strings in C++ must open and close with quotes."
        },
        {
            "story": "The robot is missing a semicolon in its power logic.",
            "code": "int battery = 100\nint voltage = 5;",
            "options": ["Remove int", "Change 100 to 50","Add ; after 100"],
            "correct": 2,
            "hint": "Most lines in C++ must end with a semicolon."
        },
        {
            "story": "Robo-X walks forever. Fix its movement logic.",
            "code": "for(int i=1; i<=5; i--) {\n  cout << i;\n}",
            "options": ["Remove loop","Change i-- to i++", "Change <="],
            "correct": 1,
            "hint": "To count up, you must use the increment operator (i++)."
        },
        {
            "story": "Energy calculation is wrong. Debug the function.",
            "code": "int add(int a, int b) {\n  return a - b;\n}",
            "options": ["Change - to +", "Change int to float", "Remove return"],
            "correct": 0,
            "hint": "Addition requires the + operator."
        },
        {
            "story": "The bot is trying to store text in a number variable.",
            "code": 'int name = "Robo-X";',
            "options": ["Remove quotes", "Change int to bool","Change int to string"],
            "correct": 2,
            "hint": "Text requires the 'string' data type."
        },
        {
            "story": "Robo-X thinks 10 is equal to 5. Fix the comparison.",
            "code": "if (x = 5) {\n  cout << 'Equal';\n}",
            "options": ["Change = to ==", "Change 5 to 10", "Add semicolon"],
            "correct": 0,
            "hint": "Comparison uses ==. A single = is for assignment."
        }
    ]

    # 2. Fetch questions from the Database (Admin Panel)
    db_questions = Question.objects.prefetch_related('options').order_by('order')
    
    for q in db_questions:
        options_list = list(q.options.all())
        correct_idx = 0
        for i, opt in enumerate(options_list):
            if opt.is_correct:
                correct_idx = i
        
        # Add the Admin questions to the list
        game_levels.append({
            "story": q.story,
            "code": q.code,
            "options": [opt.text for opt in options_list],
            "correct": correct_idx,
            "hint": q.hint
        })

    return render(request, 'index.html', {
        'levels_json': json.dumps(game_levels)
    })