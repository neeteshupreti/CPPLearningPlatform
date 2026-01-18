# Merge Summary: chat00 and accounts00 Integration

## Overview
Successfully merged code from `chat00` and `accounts00` folders into the main `chat` and `accounts` folders.

## Changes Made

### Chat App (`chat/` folder)

#### 1. **chat/models.py**
- Added `ChatMessage` model with fields:
  - `user_message` (TextField)
  - `bot_response` (TextField)
  - `timestamp` (DateTimeField with auto_now_add)

#### 2. **chat/views.py**
- Added `ask_groq()` function to integrate with Groq API
- Implemented `chat_view()` to handle:
  - POST requests for sending messages to Groq API
  - GET requests to display all chat history
  - Saves chat messages to database

#### 3. **chat/urls.py**
- Added app_name = "chat" for namespace
- Route: `path("", chat_view, name="chat")`

#### 4. **chat/admin.py**
- Registered `ChatMessage` model in Django admin
- Added list display: user_message, timestamp
- Added search and filter capabilities

### Accounts App (`accounts/` folder)

#### 1. **accounts/models.py**
- Added `ContactMessage` model with fields:
  - `name` (CharField, max_length=100)
  - `email` (EmailField)
  - `subject` (CharField, max_length=150)
  - `message` (TextField)
  - `created_at` (DateTimeField with auto_now_add)

#### 2. **accounts/views.py**
- Updated with merged views:
  - `landing_view()` - Display landing page
  - `home()` - Alias for landing page
  - `register_view()` - User registration with validation
  - `login_view()` - User login authentication
  - `dashboard_view()` - Protected dashboard (login_required)
  - `logout_view()` - User logout
  - `contact_view()` - Contact form submission (NEW)

#### 3. **accounts/urls.py**
- Added app_name = "accounts" for namespace
- Routes:
  - `""` → landing_view (name="landing")
  - `home/` → home view (name="home")
  - `signup/` → register_view (name="signup")
  - `login/` → login_view (name="login")
  - `dashboard/` → dashboard_view (name="dashboard")
  - `logout/` → logout_view (name="logout")
  - `contact/` → contact_view (name="contact") [NEW]

#### 4. **accounts/forms.py** (NEW FILE)
- Created `ContactForm` ModelForm
- Fields: name, email, subject, message
- Added Bootstrap CSS classes for styling

#### 5. **accounts/admin.py**
- Registered `ContactMessage` model
- Added list display: name, email, subject, created_at
- Added list filters and search fields

#### 6. **accounts/templates/accounts/contact.html** (NEW TEMPLATE)
- Contact form page with:
  - Form fields with Bootstrap styling
  - Error message handling
  - Success messages
  - Navigation links

### Database

#### Migrations
- Created and applied migration: `accounts/migrations/0001_initial.py`
- Migration creates the `ContactMessage` table

## Testing

✓ All imports verified successfully:
  - ContactMessage model loaded
  - ContactForm form loaded
  - ChatMessage model loaded

✓ Django system check passed (4 warnings about AutoField are non-critical)

## Configuration Notes

### Groq API Setup Required
The chat functionality requires:
1. Set `GROQ_API_KEY` in [chat/views.py](chat/views.py#L10)
2. Install `requests` package (already in requirements.txt)

### Example Usage

**Contact Form:**
```
POST /accounts/contact/
Saves contact messages to database
Displays success message on submission
```

**Chat:**
```
GET /chat/ - Display chat history
POST /chat/ - Send message to Groq API
```

## Files Modified/Created

### Modified:
- [accounts/models.py](accounts/models.py)
- [accounts/views.py](accounts/views.py)
- [accounts/urls.py](accounts/urls.py)
- [accounts/admin.py](accounts/admin.py)
- [chat/models.py](chat/models.py)
- [chat/views.py](chat/views.py)
- [chat/admin.py](chat/admin.py)

### Created:
- [accounts/forms.py](accounts/forms.py)
- [accounts/templates/accounts/contact.html](accounts/templates/accounts/contact.html)
- [accounts/migrations/0001_initial.py](accounts/migrations/0001_initial.py)

## Next Steps

1. Add Groq API key to chat/views.py
2. Test contact form submission
3. Test chat functionality with Groq API
4. Customize templates as needed
5. Update landing.html to include contact form link
