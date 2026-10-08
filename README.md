# Complete Social Media Platform - Django

## Project Overview

A Django-based social media platform developed for Month 2 web development. The project provides user accounts and profiles, posts with optional media uploads, comments, likes, friendship, following/followers, notifications, public profiles, user search, and private messaging.

## Tech Stack

- Python 3.11.x
- Django 5.2.17
- SQLite for local development
- Bootstrap 5.3.3
- Pillow for image uploads

## Applications

```text
users/             User registration, login, logout and profiles
posts/             Posts, media, likes and comments
friends/           Friends, follow/followers, notifications and public profiles
messaging/        Private messaging, inbox and conversations
social_platform/  Global settings and root URL routing
templates/         Shared base template / navigation
```

## Main Features

- User registration, login and logout
- User profile extension with profile picture and cover photo fields
- Create, edit and delete posts
- Optional post image uploads
- Like and comment systems
- Friend requests and accepted friends
- Follow and unfollow
- Followers and following views
- Notifications
- Public user profiles with statistics and posts
- Username search
- Private one-to-one messaging
- Inbox and conversation history
- Read/unread message state
- Shared navigation bar

## Setup

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
py -3.11 -m venv venv
& .\venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Run migrations

```powershell
python manage.py migrate
```

### 4. Check the project

```powershell
python manage.py check
python manage.py makemigrations --check
```

### 5. Start the development server

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## Important URLs

| URL | Purpose |
|---|---|
| `/users/` | Home page |
| `/users/login/` | Login |
| `/users/register/` | Registration |
| `/users/profile/` | Logged-in profile |
| `/posts/` | Social feed |
| `/posts/create/` | Create post |
| `/friends/` | Friends dashboard |
| `/friends/users/` | Search users / follow |
| `/friends/profile/<username>/` | Public profile |
| `/friends/notifications/` | Notifications |
| `/messages/` | Inbox |
| `/messages/chat/<username>/` | Private conversation |

## Project Structure

```text
social_platform/
├── friends/
├── messaging/
├── posts/
├── users/
├── templates/
├── manage.py
├── requirements.txt
└── .gitignore
```

## Documentation

See `Social_Platform_Documentation.pdf` for the project overview, objectives, architecture, requirements mapping, setup instructions, URL/endpoint documentation, deployment guide, user manual, screenshots, testing evidence, and submission checklist.

## Verification

The final project was verified locally with:

```text
python manage.py check
System check identified no issues (0 silenced).

python manage.py makemigrations --check
No changes detected
```

## Scope Notes

The current verified implementation uses Django server-rendered pages and form POSTs rather than a separate Django REST Framework API. Notifications are database-backed notification records; no WebSocket-based live-push channel was verified.

## Submission

- GitHub Repository URL: `[PASTE YOUR PUBLIC GITHUB REPOSITORY URL HERE]`
- Documentation URL: `[PASTE YOUR SHAREABLE DOCUMENTATION URL HERE]`
