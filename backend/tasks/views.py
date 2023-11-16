from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.http import JsonResponse

from .models import *
from .serializers import *

class TaskView(APIView):
    serializer_class = TaskSerializer

    def get(self, request, format=None):
        tasks = Task.objects.filter(user_id=request.user.id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        task = request.data.get('task')
        
        serializer = CreateTaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
        return Response({"success": "Task '{}' created successfully".format(task_saved.title)})


class LoginView(APIView):
    def post(self, request):
        data = request.data.get('user')
        if data['username'] == '':
            return JsonResponse({'status':'false','message':"No username provided"}, status=400)
        new_user = User.objects.create_user(**data)
        return Response({"success": "User '{}' created successfully".format(new_user)})
    
