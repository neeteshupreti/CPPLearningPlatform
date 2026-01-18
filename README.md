# C++ StoryLearn - Interactive Learning Platform 🚀

A modern Django web application for learning C++ programming through interactive storytelling, AI-powered tutoring, and gamification.

**Status**: ✅ **FULLY OPERATIONAL** - All systems integrated and tested

## 🎯 Features

- **📚 Story-Based Learning** - Learn C++ through engaging interactive missions
- **💬 AI Tutor** - Get instant help from Groq AI-powered chatbot (Llama 3.1)
- **🎮 Interactive Challenges** - Test your knowledge with multiple-choice questions
- **👤 User Dashboard** - Track progress and access all features in one place
- **📧 Contact Form** - Send feedback and messages to administrators
- **📊 Progress Tracking** - Monitor your learning journey with personal statistics
- **🏆 Leaderboard** - Compete with other learners
- **🔐 Secure Authentication** - User registration, login, and session management
- **📱 Responsive Design** - Works seamlessly on desktop, tablet, and mobile devices

## 🛠️ Tech Stack

- **Backend:** Django 4.2 (Python)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** SQLite3 (development) / PostgreSQL (production)
- **AI API:** Groq (Llama 3.1 8B model)
- **Auth:** Django's built-in authentication system
- **Icons:** Font Awesome 6.5

## 📋 Requirements

- Python 3.11+
- Django 4.2
- requests library
- sqlite3 (included)
- Virtual environment

## 🚀 Quick Start

### 1. Navigate to Project
```bash
cd /home/neetesh/DevWorks/aspireBootcamp/CPPLearning
```

### 2. Activate Virtual Environment
```bash
source venv/bin/activate
```

### 3. Optional: Add Groq API Key
Edit `.env` file and add:
```
GROQ_API_KEY=your_api_key_from_console.groq.com
```

### 4. Start Development Server
```bash
python manage.py runserver
```

### 5. Access the Application
Open your browser and go to: **http://localhost:8000**

### 6. Create Admin Account (Optional)
```bash
python manage.py createsuperuser
```
Then visit: **http://localhost:8000/admin**

## 📱 Main Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Landing page with feature overview |
| Register | `/signup/` | Create new account |
| Login | `/login/` | Sign in to your account |
| Dashboard | `/dashboard/` | User profile and progress tracking |
| AI Tutor | `/chat/` | Chat with AI for C++ help |
| Missions | `/game/` | Interactive coding challenges |
| Contact | `/contact/` | Send messages and feedback |
| Admin | `/admin/` | Manage users and content |

## 🏗️ Project Structure

```
CPPLearning/
├── accounts/                    # User management app
│   ├── models.py               # ContactMessage model
│   ├── views.py                # Auth & contact views
│   ├── forms.py                # ContactForm
│   ├── urls.py                 # Account routes
│   └── templates/accounts/
│       ├── landing.html        # Home page
│       ├── login.html
│       ├── register.html
│       ├── dashboard.html
│       └── contact.html
│
├── chat/                        # AI tutoring app
│   ├── models.py               # ChatMessage model
│   ├── views.py                # Chat + Groq API
│   ├── urls.py                 # Chat routes
│   ├── admin.py                # Admin interface
│   └── templates/chat/
│       └── chat.html           # Chat interface
│
├── game/                        # Missions app
│   ├── models.py               # Question, Option models
│   ├── views.py                # Game logic
│   ├── urls.py                 # Game routes
│   └── templates/game/
│       ├── home.html
│       ├── quiz.html
│       ├── result.html
│       └── leaderboard.html
│
├── templates/                   # Shared templates
│   ├── base.html               # Main layout
│   └── index.html              # Alternative home
│
├── RoboQuiz/                    # Project settings
│   ├── settings.py             # Django configuration
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py
│   └── asgi.py
│
├── .env                         # Environment variables
├── requirements.txt             # Python dependencies
└── manage.py                    # Django management
```

## 🔑 Key Features Explained

### User Authentication
- Register with email and password
- Secure login with session management
- Password confirmation validation
- Protected views (dashboard, chat, contact)

### AI Chat (Groq Integration)
- Real-time chat interface
- Powered by Llama 3.1 8B model
- Store chat history in database
- Read more/less for long responses

### Contact Form
- Submit messages with validation
- Stored in database for admin review
- Success notifications
- Bootstrap-styled form

### Dashboard
- Welcome message
- Progress statistics
- Quick action buttons
- Achievement tracking
- Account settings

## ⚙️ Configuration

### Environment Variables (.env)
```
DEBUG=True
SECRET_KEY=your-secret-key
GROQ_API_KEY=your-groq-api-key
```

### Getting Groq API Key
1. Visit https://console.groq.com
2. Sign up or login
3. Create API key
4. Add to .env file

## 🧪 Testing

Run system integration test:
```bash
python test_system.py
```

View system status:
```bash
python show_status.py
```

## 📚 Documentation

- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
- **[COMPLETE_SETUP_GUIDE.md](COMPLETE_SETUP_GUIDE.md)** - Detailed setup
- **[SYSTEM_STATUS.md](SYSTEM_STATUS.md)** - System overview
- **[MERGE_SUMMARY.md](MERGE_SUMMARY.md)** - Integration details

## 🐛 Troubleshooting

### Chat not working?
- Add Groq API key to `.env`
- Check internet connection
- Restart development server

### Page not loading?
- Verify URL spelling
- Check if you're logged in (for protected pages)
- Clear browser cache

### Database errors?
- Run: `python manage.py migrate`
- Ensure db.sqlite3 exists
- Check file permissions

## 🚀 Deployment

For production deployment:
1. Set `DEBUG=False` in settings
2. Generate strong `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use PostgreSQL instead of SQLite
5. Enable HTTPS
6. Configure email backend

## 📞 Support

For issues:
1. Check documentation files
2. Review console output
3. Run integration tests
4. Check `.env` configuration

## 🎓 Learning Resources

- [Django Docs](https://docs.djangoproject.com/)
- [Groq API Docs](https://console.groq.com/docs)
- [C++ Reference](https://en.cppreference.com/)
- [Bootstrap Docs](https://getbootstrap.com/)

## 🤝 Contributing

To contribute:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 👨‍💻 Authors

- **You** - Full stack developer
- **AI** - Code assistance

## 🎉 Current Status

✅ **Version 1.0 - Complete Release**

- ✅ All apps merged and integrated
- ✅ All features implemented
- ✅ System tested and verified
- ✅ Documentation complete
- ✅ Ready for deployment

Start learning C++ today! 🚀

---

**Last Updated**: January 18, 2026  
**Status**: ✅ Production Ready (with API key configuration)
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
