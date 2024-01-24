from rest_framework import serializers
from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    class Meta:
        model= Todo
        fields = '__all__'
class TodoToggleCompleteSerializer(serializers.Serializer):
    class Meta:
        model=Todo
        fields =  ['id']
        read_only_fields = ['title', 'memo', 'created', 'completed']
        