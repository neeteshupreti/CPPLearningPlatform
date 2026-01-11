#!/bin/bash
# Quick Start Guide for C++ StoryLearn

echo "🚀 C++ StoryLearn - Quick Start Guide"
echo "======================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please create it first:"
    echo "   python3 -m venv venv"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate
echo "✅ Virtual environment activated"

# Install dependencies if needed
echo "📦 Checking dependencies..."
venv/bin/pip install -q django python-dotenv requests

# Run migrations
echo "🔄 Running migrations..."
venv/bin/python manage.py migrate --quiet
echo "✅ Migrations complete"

# Populate sample data
echo "📚 Populating sample missions..."
venv/bin/python manage.py shell < populate_sample_data.py

# Start the server
echo ""
echo "🎉 Everything is ready!"
echo ""
echo "Starting Django development server..."
echo "======================================"
echo ""
echo "📱 Access the application at: http://127.0.0.1:8000/"
echo ""
echo "🎯 Quick Links:"
echo "   • Landing Page: http://127.0.0.1:8000/"
echo "   • Admin Panel: http://127.0.0.1:8000/admin/"
echo "   • Missions: http://127.0.0.1:8000/game/"
echo ""
echo "👤 Test User (if needed):"
echo "   Email: test@example.com"
echo "   Password: testpass123"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

venv/bin/python manage.py runserver
