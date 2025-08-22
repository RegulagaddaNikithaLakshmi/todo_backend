# todo/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# ModelViewSet automatically provides the full set of CRUD operations:
# - create()
# - retrieve()
# - list()
# - update() / partial_update()
# - destroy()
class TodoViewSet(viewsets.ModelViewSet):
    # Specifies the queryset to be used for the viewset.
    queryset = Todo.objects.all()
    
    # Specifies the serializer to use for data validation and formatting.
    serializer_class = TodoSerializer

    # This is a custom action to handle the "mark as read" requirement.
    # It creates a new endpoint at `/api/todos/<id>/mark_as_read/`.
    @action(detail=True, methods=['put'])
    def mark_as_read(self, request, pk=None):
        # Use get_object() to retrieve the specific todo by its primary key (pk).
        todo = self.get_object()
        # Update the 'completed' field to True.
        todo.completed = True
        # Save the changes to the database.
        todo.save()
        # Return a success response.
        return Response({'status': 'Todo marked as completed'}, status=status.HTTP_200_OK)


# Create your views here.
