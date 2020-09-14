from rest_framework.serializers import ModelSerializer
from todolist.task.models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model= Task
        fields= ['id','task', 'checked', 'user']