# C++ StoryLearn - Complete System Setup Guide

## Project Overview
C++ StoryLearn is a comprehensive learning platform that combines interactive storytelling, coding challenges, and AI-powered tutoring to help users master C++ programming.

## System Architecture

### Apps Included
1. **Accounts App** - User authentication and management
   - Login/Register
   - Dashboard
   - Profile management
   - Contact form

2. **Chat App** - AI-powered tutoring system
   - Groq API integration (Llama 3.1 8B model)
   - Real-time chat messaging
   - Chat history storage
   - Message management

3. **Game App** - Interactive coding missions
   - Story-based learning missions
   - Coding challenges
   - Leaderboard
   - Progress tracking

## Features Implemented

### ✅ User Authentication
- User registration with email and password
- Login system with session management
- Password confirmation validation
- Logout functionality
- Login-required protection for dashboard

### ✅ Dashboard
- Welcome message with user name
- Progress statistics
- Active missions display
- AI Tutor quick access
- Leaderboard ranking
- Achievement tracking
- Account settings

### ✅ AI Tutor (Chat)
- Real-time chat interface
- Groq API integration
- Message history storage in database
- Read more/Read less functionality
- Loading indicators
- Error handling with user-friendly messages
- CSRF protection for security

### ✅ Contact Form
- Contact message submission
- Form validation
- Database storage
- Success/error messaging
- Bootstrap-styled form

### ✅ Navigation
- Responsive navbar with all major routes
- Dynamic navigation based on authentication status
- Quick links on landing page
- Feature cards with action buttons

### ✅ Templates
- Base template with consistent styling
- Landing page with feature showcase
- Login and registration pages
- Dashboard with statistics
- Chat interface with message display
- Contact form page

## File Structure

```
CPPLearning/
├── accounts/                    # User management app
│   ├── migrations/
│   │   └── 0001_initial.py    # ContactMessage model migration
│   ├── templates/accounts/
│   │   ├── landing.html       # Home page
│   │   ├── login.html         # Login page
│   │   ├── register.html      # Registration page
│   │   ├── dashboard.html     # User dashboard
│   │   └── contact.html       # Contact form
│   ├── admin.py               # ContactMessage admin registration
│   ├── forms.py               # ContactForm
│   ├── models.py              # ContactMessage model
│   ├── views.py               # All view functions
│   ├── urls.py                # URL routing
│   └── apps.py                # App configuration
│
├── chat/                       # AI tutoring app
│   ├── migrations/            # Existing migrations
│   ├── templates/chat/
│   │   └── chat.html          # Chat interface
│   ├── admin.py               # ChatMessage admin registration
│   ├── models.py              # ChatMessage model
│   ├── views.py               # Chat view with Groq API integration
│   ├── urls.py                # Chat URL routing
│   └── apps.py                # App configuration
│
├── game/                       # Mission/challenge app
│   ├── migrations/            # Game app migrations
│   ├── templates/game/
│   │   ├── home.html
│   │   ├── quiz.html
│   │   ├── result.html
│   │   └── leaderboard.html
│   ├── models.py              # Game models
│   ├── views.py               # Game views
│   ├── urls.py                # Game routing
│   └── apps.py                # App configuration
│
├── templates/                  # Global templates
│   ├── base.html              # Base template with navbar
│   └── index.html             # Alternative index
│
├── RoboQuiz/                   # Main project settings
│   ├── settings.py            # Django settings + Groq API config
│   ├── urls.py                # Main URL routing
│   ├── wsgi.py                # WSGI configuration
│   ├── asgi.py                # ASGI configuration
│   └── views.py               # Project-level views
│
├── .env                        # Environment variables (created)
├── requirements.txt            # Python dependencies
├── manage.py                   # Django management script
└── db.sqlite3                  # SQLite database
```

## Configuration

### Environment Variables (.env file)

```
# Django Settings
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here

# Groq API
GROQ_API_KEY=your_groq_api_key_here

# Email (Optional)
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Getting Groq API Key

1. Visit [https://console.groq.com](https://console.groq.com)
2. Sign up or log in with your account
3. Create a new API key
4. Copy the key
5. Paste it in `.env` file:
   ```
   GROQ_API_KEY=gsk_xxxxxxxxxxxxx
   ```

## Running the Application

### Start the Development Server
```bash
cd /home/neetesh/DevWorks/aspireBootcamp/CPPLearning
source venv/bin/activate
python manage.py runserver
```

### Access the Application
- Home: http://localhost:8000/
- Login: http://localhost:8000/login/
- Register: http://localhost:8000/signup/
- Dashboard: http://localhost:8000/dashboard/
- Chat: http://localhost:8000/chat/
- Missions: http://localhost:8000/game/
- Admin: http://localhost:8000/admin/

## Database Models

### ContactMessage (accounts app)
- name: CharField (max_length=100)
- email: EmailField
- subject: CharField (max_length=150)
- message: TextField
- created_at: DateTimeField (auto_now_add)

### ChatMessage (chat app)
- user_message: TextField
- bot_response: TextField
- timestamp: DateTimeField (auto_now_add)

### Question, Option (game app)
- Various fields for quiz/mission content

## URL Routes

### Accounts URLs
- `/` - Landing page (name: landing)
- `/home/` - Home view (name: home)
- `/signup/` - Register view (name: signup)
- `/login/` - Login view (name: login)
- `/dashboard/` - Dashboard (name: dashboard)
- `/logout/` - Logout (name: logout)
- `/contact/` - Contact form (name: contact)

### Chat URLs
- `/chat/` - Chat interface (name: chat)

### Game URLs
- `/game/` - Game home (name: home)
- `/game/leaderboard/` - Leaderboard (name: leaderboard)

### Admin
- `/admin/` - Django admin

## API Integration

### Groq API
- **Endpoint**: https://api.groq.com/openai/v1/chat/completions
- **Model**: llama-3.1-8b-instant
- **Auth**: Bearer token in Authorization header
- **Usage**: Ask C++ programming questions to the AI tutor

## Features Summary

✅ User authentication (login/register)
✅ Secure dashboard
✅ AI-powered chat tutoring
✅ Chat message history
✅ Contact form with database storage
✅ Responsive design with Bootstrap
✅ Admin panel for content management
✅ URL namespacing for routing
✅ Environment variable support
✅ Error handling and user feedback
✅ CSRF protection
✅ Database migrations

## Known Limitations

- Groq API key must be configured in .env file for chat to work
- API responses depend on internet connectivity
- Rate limiting may apply with Groq API free tier

## Next Steps

1. **Add Groq API Key**
   - Visit https://console.groq.com
   - Generate API key
   - Add to .env file

2. **Test Chat Feature**
   - Login to the application
   - Navigate to "AI Tutor"
   - Ask C++ questions

3. **Customize Templates**
   - Update landing page with your branding
   - Customize colors and styling
   - Add more feature cards

4. **Production Deployment**
   - Change DEBUG=False in .env
   - Set a strong SECRET_KEY
   - Configure allowed hosts
   - Set up proper email backend
   - Use environment-specific settings

## Support

For issues or questions:
- Use the Contact form in the application
- Check Django logs for error messages
- Verify Groq API key is properly configured

## Project Status

✅ **Complete and Ready to Use**
- All core features implemented
- All apps integrated
- Database migrations applied
- Environment configuration ready
- Old folders (chat00, accounts00) removed

---
**Last Updated**: January 18, 2026
**Version**: 1.0
