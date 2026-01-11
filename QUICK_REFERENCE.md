# Quick Reference Card - C++ StoryLearn

## 🎯 Project Quick Facts

- **Project Name:** C++ StoryLearn
- **Type:** Django Web Application (MVT)
- **Status:** ✅ Complete and Running
- **Server:** http://127.0.0.1:8000
- **Python Version:** 3.12
- **Django Version:** 6.0

---

## 📍 Main URLs

| URL | Purpose | Auth Required |
|-----|---------|---|
| `/` | Landing Page | No |
| `/signup/` | Register | No |
| `/login/` | Login | No |
| `/dashboard/` | User Dashboard | Yes |
| `/logout/` | Logout | Yes |
| `/game/` | All Missions | Yes |
| `/game/quiz/<id>/` | Take Quiz | Yes |
| `/game/leaderboard/` | Leaderboard | Yes |
| `/chat/` | AI Tutor | Yes |
| `/admin/` | Admin Panel | Yes (Admin) |

---

## 🏗️ Project Structure

```
Accounts     →  User Management (Auth)
├── Views: register, login, dashboard
├── Templates: 4 responsive HTML files
└── URL: / /signup/ /login/ /dashboard/ /logout/

Game        →  Quiz & Missions
├── Views: missions, quiz, check, leaderboard
├── Models: Question, Option
├── Templates: 4 HTML files
└── URL: /game/ /game/quiz/ /game/check/ /game/leaderboard/

Chat        →  AI Tutor
├── Views: chat interface
├── Models: ChatMessage
├── Templates: chat.html
└── URL: /chat/

Templates   →  Base & Styling
└── base.html (Main layout template)
```

---

## 🎨 Key Features

✅ User Registration & Login
✅ Protected Pages (Requires Login)
✅ C++ Quiz Missions
✅ Answer Validation with Hints
✅ Leaderboard & Rankings
✅ AI Chatbot (Groq API)
✅ User Dashboard
✅ Responsive Design
✅ Modern UI with Gradients
✅ Mobile Friendly

---

## 🚀 Quick Start

```bash
# Terminal 1: Start Server
cd /home/neetesh/Documents/aspireBootcamp/week2Quiz
./venv/bin/python manage.py runserver

# Terminal 2: Load Sample Data (optional)
cd /home/neetesh/Documents/aspireBootcamp/week2Quiz
./venv/bin/python manage.py shell < populate_sample_data.py

# Open in Browser
http://127.0.0.1:8000/
```

---

## 📝 Key Files

| File | Purpose |
|------|---------|
| `RoboQuiz/settings.py` | Django configuration |
| `RoboQuiz/urls.py` | Main URL router |
| `templates/base.html` | Master template |
| `accounts/views.py` | User views |
| `game/views.py` | Mission views |
| `chat/views.py` | Chat view |
| `game/models.py` | Database models |

---

## 🎓 Test Users

Create your own via `/signup/` or via Django shell:

```python
from django.contrib.auth.models import User
User.objects.create_user(
    username='test@example.com',
    email='test@example.com',
    password='password123',
    first_name='Test',
    last_name='User'
)
```

---

## 🔑 Django Admin

```bash
# Create Admin Account
./venv/bin/python manage.py createsuperuser

# Access Admin
http://127.0.0.1:8000/admin/

# Add Missions in Admin:
1. Go to Questions
2. Add story, code, hint, order
3. Create Options
4. Mark correct answers
```

---

## 🎯 Add Missions

### Via Python Script
```bash
./venv/bin/python manage.py shell < populate_sample_data.py
```

### Via Django Admin
```
1. http://127.0.0.1:8000/admin/
2. Game > Questions > Add Question
3. Fill: story, code, hint, order
4. Save
5. Add Options to the question
```

---

## 🔧 Configuration

### Enable Groq AI Chat
Edit `chat/views.py`:
```python
GROQ_API_KEY = "your_actual_key_here"
```

### Change Colors
Edit `templates/base.html`:
```css
Primary: #0056D2 → Your color
Secondary: #FFC107 → Your color
```

### Change Site Title
Edit `settings.py` or individual templates

---

## 📊 Database Models

### User (Django Built-in)
```
id, username, email, password, first_name, last_name, date_joined
```

### Question (Game)
```
id, story, code, hint, order
```

### Option (Game)
```
id, question_id, text, is_correct
```

### ChatMessage (Chat)
```
id, user_message, bot_response, timestamp
```

---

## 🧪 Common Commands

```bash
# Run server
./venv/bin/python manage.py runserver

# Run migrations
./venv/bin/python manage.py migrate

# Create superuser
./venv/bin/python manage.py createsuperuser

# Interactive shell
./venv/bin/python manage.py shell

# Check configuration
./venv/bin/python manage.py check

# Load data
./venv/bin/python manage.py shell < populate_sample_data.py

# Collect static (production)
./venv/bin/python manage.py collectstatic
```

---

## 🔐 Security Features

✅ CSRF Protection
✅ Password Hashing
✅ SQL Injection Prevention
✅ XSS Protection
✅ Session Management
✅ Login Required Decorators
✅ Admin Authentication

---

## 📱 Responsive Breakpoints

- **Desktop:** > 1200px (Full)
- **Tablet:** 768-1200px (Adjusted)
- **Mobile:** < 768px (Optimized)

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Server won't start | Check port 8000 not in use, or use different port |
| Template not found | Run: `./venv/bin/python manage.py check` |
| Database error | Run: `./venv/bin/python manage.py migrate` |
| Import error | Install: `./venv/bin/pip install [package]` |
| Static files missing | Run: `./venv/bin/python manage.py collectstatic` |

---

## 📚 Learn More

- Django Docs: https://docs.djangoproject.com/
- Python: https://www.python.org/
- HTML/CSS: https://developer.mozilla.org/
- Groq API: https://console.groq.com/

---

## ✨ What's Next

1. ✅ App is running
2. Create test account
3. Load sample missions
4. Take quizzes
5. Configure API keys
6. Deploy to production

---

**Status:** ✅ Complete & Ready to Use
**Last Updated:** January 11, 2026
