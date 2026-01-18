# C++ StoryLearn - Architecture Diagram

## Overall Application Flow

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│              C++ STORYLEARN APPLICATION                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘

                    ┌──────────────────┐
                    │   User Browser   │
                    │  (Web Client)    │
                    └────────┬─────────┘
                             │
                             │ HTTP Requests
                             │
                    ┌────────▼─────────┐
                    │  Django Server   │
                    │  port 8000       │
                    └────────┬─────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
      ┌─────▼────┐    ┌─────▼────┐    ┌──────▼───┐
      │ Accounts │    │   Game   │    │  Chat   │
      │   App    │    │   App    │    │   App   │
      └─────┬────┘    └─────┬────┘    └──────┬──┘
            │               │               │
      ┌─────▼────┐    ┌─────▼────┐    ┌──────▼───┐
      │   User   │    │Question  │    │ChatMsg  │
      │ Management│   │  &Option │    │ Storage │
      └──────────┘    └──────────┘    └─────────┘
            │               │               │
            └───────┬───────┴───────┬──────┘
                    │
            ┌───────▼────────┐
            │  SQLite3 DB    │
            │  (db.sqlite3)  │
            └────────────────┘
```

## URL Routing Structure

```
http://127.0.0.1:8000/
│
├── / (Landing Page)
│   ├── /signup/       (User Registration)
│   ├── /login/        (User Login)
│   └── [Protected Routes Below]
│
├── /dashboard/        (User Dashboard)
│
├── /game/             (Game Home)
│   ├── /game/quiz/<id>/       (Take Quiz)
│   ├── /game/check/<id>/      (Submit Answer)
│   └── /game/leaderboard/     (Rankings)
│
├── /chat/             (AI Tutor)
│
├── /logout/           (Logout)
│
└── /admin/            (Django Admin)
```

## Template Inheritance Tree

```
                    ┌──────────────────┐
                    │   base.html      │
                    │  (Master Template)│
                    │                  │
                    │ ✨ Features:     │
                    │ • Navbar         │
                    │ • Messages       │
                    │ • Styling        │
                    │ • Footer         │
                    └────────┬─────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
    ┌───▼────┐           ┌───▼────┐         ┌────▼────┐
    │Accounts│           │  Game  │         │  Chat   │
    │Folder  │           │ Folder │         │ Folder  │
    └───┬────┘           └───┬────┘         └────┬────┘
        │                    │                    │
    ┌───▼──────────┐     ┌───▼──────────┐   ┌────▼───────┐
    │landing.html  │     │home.html     │   │chat.html   │
    │register.html │     │quiz.html     │   └────────────┘
    │login.html    │     │result.html   │
    │dashboard.html│     │leaderboard.html
    └──────────────┘     └──────────────┘
```

## Model Relationships

```
┌─────────────────────┐
│   Django User       │
│  (Built-in)         │
│                     │
│ • id                │
│ • username          │
│ • email             │
│ • password (hash)   │
│ • first_name        │
│ • last_name         │
│ • date_joined       │
└──────────┬──────────┘
           │
           │ (1 user can take many quizzes)
           │
           │         ┌──────────────┐
           │         │  Question    │
           │         │              │
           │         │ • id         │
           └────────▶│ • story      │
                     │ • code       │
                     │ • hint       │
                     │ • order      │
                     └────────┬─────┘
                              │
                              │ (1 question has many options)
                              │
                              ├──────────────┐
                              │              │
                         ┌────▼────┐    ┌───▼────┐
                         │ Option 1 │    │ Option 2│
                         │          │    │        │
                         │ • text   │    │ • text │
                         │ • correct│    │ • correct
                         │    = T   │    │    = F
                         └──────────┘    └────────┘

┌──────────────────────┐
│  ChatMessage         │
│                      │
│ • id                 │
│ • user_message       │
│ • bot_response       │
│ • timestamp          │
└──────────────────────┘
```

## Request/Response Cycle

```
1. USER REQUEST
   ┌─────────────────────────────┐
   │ User clicks link in browser  │
   │ Browser sends HTTP request   │
   └──────────────┬──────────────┘
                  │
2. DJANGO ROUTES
   ┌──────────────▼──────────────┐
   │ URLs.py matches route       │
   │ Finds appropriate view      │
   └──────────────┬──────────────┘
                  │
3. VIEW LOGIC
   ┌──────────────▼──────────────┐
   │ View receives request       │
   │ Executes business logic     │
   │ Queries database if needed  │
   │ Prepares context data       │
   └──────────────┬──────────────┘
                  │
4. TEMPLATE RENDERING
   ┌──────────────▼──────────────┐
   │ Template receives context   │
   │ Extends base.html           │
   │ Renders HTML with data      │
   │ Substitutes variables       │
   └──────────────┬──────────────┘
                  │
5. HTTP RESPONSE
   ┌──────────────▼──────────────┐
   │ Django sends HTTP response  │
   │ Browser renders HTML        │
   │ Displays to user            │
   └─────────────────────────────┘
```

## Database Schema

```
USERS TABLE (Django Built-in)
┌─────────────────────────────────┐
│ id | username | email | password│
├────┼──────────┼───────┼─────────┤
│ 1  │test@ex.c │test@..│ hashed..│
│ 2  │john@ex.c │john@..│ hashed..│
└─────────────────────────────────┘

QUESTIONS TABLE
┌──────────────────────────────────────────────────┐
│ id | story        | code | hint | order         │
├────┼──────────────┼──────┼──────┼───────────────┤
│ 1  │Variables...  │ int x│ Use =│ 1             │
│ 2  │Loops...      │ for()│ i<5  │ 2             │
└──────────────────────────────────────────────────┘

OPTIONS TABLE
┌────────────────────────────────────────┐
│ id | question_id | text | is_correct  │
├────┼─────────────┼──────┼─────────────┤
│ 1  │ 1           │ int a│ 1 (True)    │
│ 2  │ 1           │ var a│ 0 (False)   │
│ 3  │ 2           │ for()│ 1 (True)    │
└────────────────────────────────────────┘

CHATMESSAGES TABLE
┌──────────────────────────────────────────────────┐
│ id | user_message | bot_response | timestamp    │
├────┼──────────────┼──────────────┼──────────────┤
│ 1  │ Explain loop │ A loop...    │ 2026-01-11..│
│ 2  │ What's ptr?  │ Pointer is...│ 2026-01-11..│
└──────────────────────────────────────────────────┘
```

## User Journey Map

```
START
  │
  ├─ New User?
  │   └─→ /signup/ → Register → /login/ → Enter Credentials
  │
  └─ Existing User?
      └─→ /login/ → Enter Email & Password
                        │
                        ▼
                   [AUTHENTICATED]
                        │
        ┌───────────────┼───────────────┐
        │               │               │
     /dashboard/   /game/home     /chat/
        │               │               │
        │          View Missions   Ask AI
        │               │               │
        │          /game/quiz/<id>/     │
        │               │               │
        │          Answer Quiz          │
        │               │               │
        │          /game/result/        │
        │               │               │
        ▼               ▼               ▼
    [View Progress] [Check Score] [Get Help]
        │               │               │
        └───────────────┴───────────────┘
                        │
                     /logout/
                        │
                        ▼
                    [SIGNED OUT]
                        │
                        ▼
                    Back to /
```

## Authentication Flow

```
User                Browser              Django              Database
 │                    │                    │                  │
 │─ Click "Sign Up" ─→│                    │                  │
 │                    │─ GET /signup/ ────→│                  │
 │                    │←─ signup.html ─────│                  │
 │                    │                    │                  │
 │─ Fill Form ──────→│                    │                  │
 │                    │─ POST /signup/ ───→│                  │
 │                    │                    │─ Check email ───→│ Exists?
 │                    │                    │←─ No ────────────│
 │                    │                    │─ Create user ──→│
 │                    │                    │                  │
 │                    │←─ Redirect /login/─│                  │
 │                    │                    │                  │
 │─ Log in ──────────→│                    │                  │
 │                    │─ GET /login/ ─────→│                  │
 │                    │←─ login.html ──────│                  │
 │                    │                    │                  │
 │─ Enter Creds ─────→│                    │                  │
 │                    │─ POST /login/ ────→│                  │
 │                    │                    │─ Auth user ────→│ Check
 │                    │                    │←─ Success ──────│
 │                    │                    │─ Create Session─→
 │                    │←─ Redirect Dashboard
 │                    │                    │                  │
 │─ Logged In ───────→│                    │                  │
 │                    │─ GET /dashboard/ ─→│─ Verify Session→
 │                    │←─ dashboard.html ──│←─ Valid ────────│
 │                    │                    │                  │
```

## Components Relationships

```
┌────────────────────────────────────────────────────┐
│           C++ STORYLEARN COMPONENTS               │
└────────────────────────────────────────────────────┘

    FRONTEND (HTML/CSS/JS)
    ├── base.html (Master)
    ├── landing.html (Home)
    ├── register.html (Auth)
    ├── login.html (Auth)
    ├── dashboard.html (Profile)
    ├── home.html (Game)
    ├── quiz.html (Game)
    ├── result.html (Game)
    ├── leaderboard.html (Game)
    └── chat.html (Chat)

    BACKEND (Django Views)
    ├── accounts/ (Auth)
    ├── game/ (Logic)
    └── chat/ (Logic)

    DATABASE (Models)
    ├── User (Django)
    ├── Question
    ├── Option
    └── ChatMessage

    INTEGRATIONS
    ├── Font Awesome (Icons)
    ├── Groq API (AI)
    └── Django Admin (Management)

    FEATURES
    ├── Authentication
    ├── Quiz System
    ├── Leaderboard
    ├── Chat
    ├── Dashboard
    ├── Progress Tracking
    └── Gamification
```

---

## Summary

This architecture provides:
- ✅ **Clean Separation** - Views, Templates, Models separate
- ✅ **Scalability** - Easy to add new features
- ✅ **Security** - Django's built-in protections
- ✅ **Maintainability** - Well-organized code
- ✅ **Performance** - Database optimization ready
- ✅ **User Experience** - Intuitive interface

All components work together seamlessly to create an engaging learning platform!
