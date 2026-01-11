import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Replace with your actual Groq API key
GROQ_API_KEY = ""

def ask_groq(prompt):
    """
    Function to call Groq API with user prompt and return bot response.
    """
    url = "https://api.groq.com/openai/v1/chat/completions"
    payload = {
        "model": "llama-3.1-8b-instant",  # you can choose Llama3 variants
        "messages": [{"role": "user", "content": prompt}]
    }
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()

        # Check if API returned 'choices'
        if "choices" in data and len(data["choices"]) > 0:
            return data["choices"][0]["message"]["content"]
        else:
            # API error or invalid response
            return f"Groq API Error: {data.get('error', 'No response from API')}"
    except Exception as e:
        return f"Exception calling Groq API: {str(e)}"


def chat_view(request):
    """
    View to handle displaying chat and sending user messages to Groq.
    """
    if request.method == "POST":
        user_msg = request.POST.get("message", "").strip()
        if not user_msg:
            return JsonResponse({"response": "Please type a message."})

        # Call Groq API
        bot_reply = ask_groq(user_msg)

        # Save chat in DB
        ChatMessage.objects.create(user_message=user_msg, bot_response=bot_reply)

        return JsonResponse({"response": bot_reply})

    # GET request: display all chats
    chats = ChatMessage.objects.all().order_by("timestamp")
    return render(request, "chat/chat.html", {"messages": chats})
