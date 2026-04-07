from django.db import models
from django.contrib.auth.models import User # Django ka built-in User model

class Todo(models.Model):
    # 'on_delete=models.CASCADE' ka matlab hai agar user delete hua toh uske tasks bhi delete ho jayein
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title