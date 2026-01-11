# C++ StoryLearn - Interactive Learning Platform 🚀

A modern Django web application for learning C++ programming through interactive storytelling, AI-powered tutoring, and gamification.

## 🎯 Features

- **📚 Story-Based Learning** - Learn C++ through engaging interactive missions
- **🎮 Interactive Quizzes** - Test your knowledge with multiple-choice questions
- **💡 AI Tutor** - Get instant help from an AI-powered chatbot powered by Groq
- **🏆 Gamification** - Earn XP points, earn badges, and climb the leaderboard
- **📊 Progress Tracking** - Monitor your learning journey with a personal dashboard
- **📱 Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices
- **🔐 Secure Authentication** - User registration, login, and session management

## 🛠️ Tech Stack

- **Backend:** Django 6.0 (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3 (included) / PostgreSQL (optional)
- **UI Framework:** Custom responsive design with Font Awesome icons
- **API:** Groq AI for chatbot functionality

## 📋 Requirements

- Python 3.12+
- Django 6.0
- SQLite3 (included with Python)
- pip (Python package manager)

## 🚀 Quick Start

### 1. Navigate to Project
```bash
cd /home/neetesh/Documents/aspireBootcamp/week2Quiz
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Start Development Server
```bash
python manage.py runserver
```

### 4. Access the Application
Open your browser and go to: **http://127.0.0.1:8000/**

### 5. Load Sample Data (Optional)
```bash
python manage.py shell < populate_sample_data.py
```

## 📖 Documentation

- **[Project Implementation Guide](./PROJECT_IMPLEMENTATION_GUIDE.md)** - Comprehensive guide with all details
- **[MVT Implementation Summary](./MVT_IMPLEMENTATION_SUMMARY.md)** - Overview of the MVT architecture
- **[Quick Reference Card](./QUICK_REFERENCE.md)** - Quick lookup for common tasks
- **[Completion Checklist](./COMPLETION_CHECKLIST.md)** - What has been implemented

## 🗂️ Project Structure

```
RoboQuiz/
├── accounts/                    # User authentication
│   ├── views.py                # Registration, login, dashboard
│   ├── urls.py                 # Account routes
│   ├── models.py               # User models
│   └── templates/accounts/     # HTML templates
│
├── game/                        # Quiz and missions
│   ├── views.py                # Game logic
│   ├── urls.py                 # Game routes
│   ├── models.py               # Question, Option models
│   └── templates/game/         # Quiz templates
│
├── chat/                        # AI tutor
│   ├── views.py                # Chat logic
│   ├── urls.py                 # Chat routes
│   ├── models.py               # ChatMessage model
│   └── templates/chat/         # Chat interface
│
├── RoboQuiz/                   # Main project settings
│   ├── settings.py             # Django configuration
│   ├── urls.py                 # Main URL router
│   └── wsgi.py                 # WSGI application
│
├── templates/
│   └── base.html               # Master template
│
├── manage.py                   # Django management script
└── populate_sample_data.py     # Sample data loader
```

## 🎓 User Guide

### Creating an Account
1. Visit http://127.0.0.1:8000/
2. Click "Sign Up"
3. Fill in your details
4. Click "Create Account"
5. Log in with your credentials

### Taking a Mission
1. Log in to your account
2. Go to "Missions"
3. Click "Start" on any mission
4. Read the story and code
5. Select your answer
6. Get instant feedback

### Using the AI Tutor
1. Log in to your account
2. Go to "AI Tutor"
3. Ask any C++ question
4. Get instant answers from the AI

## 🚢 Deployment

### Before Production
1. Set `DEBUG = False` in settings.py
2. Generate a secure `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Set up a production database
5. Collect static files: `python manage.py collectstatic`

## 📞 Support

For help with:
- **Django:** https://docs.djangoproject.com/
- **Python:** https://www.python.org/
- **Groq API:** https://console.groq.com/

## ✨ Project Status

- ✅ **MVT Architecture:** Complete
- ✅ **User Authentication:** Functional
- ✅ **Quiz System:** Working
- ✅ **AI Tutor:** Ready (API key needed)
- ✅ **Responsive Design:** Mobile-friendly
- ✅ **Server:** Running successfully

---

**Built with ❤️ for Learning**

**Status:** ✅ Complete and Ready to Use
**Server:** http://127.0.0.1:8000/




## 🌟 Features

- **Gamified Learning:** Progress through missions to repair Robo-X.
- **Dynamic Content:** A hybrid system with 6 core default missions and an unlimited number of custom missions added via the Django Admin.
- **Responsive UI:** Modern, clean interface built with CSS Grid and Flexbox, fully responsive for desktop and mobile.
- **Admin Dashboard:** A powerful back-end interface for educators/developers to add new questions and hints without touching the code.
- **Real-time Feedback:** Instant validation of answers with a hint system for incorrect attempts.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript (ES6)
- **Database:** SQLite (Default)
- **Architecture:** Model-View-Template (MVT)

---

## 🚀 Installation & Setup

Follow these steps to get the project running locally:

### 1. Clone the repository
```bash
git clone [https://github.com/your-username/RoboQuiz_py.git](https://github.com/your-username/RoboQuiz_py.git)
cd RoboQuiz_py
