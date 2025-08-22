# todo/models.py
from django.db import models

# This model defines the structure of the Todo item in the database.
# Each field corresponds to a column in the 'Todo' table.
class Todo(models.Model):
    # The title of the todo item.
    title = models.CharField(max_length=100)
    
    # A longer description for the todo. 'blank=True' means it's optional.
    description = models.TextField(blank=True)
    
    # A boolean field to track if the todo is completed. 'default=False' sets the initial value.
    completed = models.BooleanField(default=False)
    
    # Automatically sets the creation timestamp when a new todo is created.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # This provides a human-readable representation of the object.
        return self.title


# Create your models here.
