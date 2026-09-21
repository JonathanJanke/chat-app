from django.shortcuts import render
from django.http import JsonResponse

from chat.models import Chat

def chat_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Save the chat message to the database
        chat = Chat.objects.create(name=name, message=message)
        return JsonResponse({'status': 'success', 'chat_id': chat.id})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def get_chats(request):
    chats = Chat.objects.all().order_by('-created_at')
    chat_list = [{'name': chat.name, 'message': chat.message, 'created_at': chat.created_at} for chat in chats]
    return JsonResponse({'chats': chat_list})

# Create your views here.
