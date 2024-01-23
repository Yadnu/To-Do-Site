from django.shortcuts import render
from rest_framework import generics
from todo.models import Todo
from .serializers import TodoSerializer
# Create your views here.
class TodoList(generics.ListAPIView):
    serializer_class=TodoSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
