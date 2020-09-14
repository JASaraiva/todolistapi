from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from todolist.task.models import Task
from todolist.task.api.serializers import TaskSerializer

class TaskViewSet(ModelViewSet):

    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication] 

    #queryset = List.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        userid = self.request.user.id
        return Task.objects.filter(user = userid)
      


    def create(self, request):

        task = {"task": request.data["task"],
           "checked": request.data["checked"],
           "user": request.user.id,
        }
        serializer = self.get_serializer(data=task)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)