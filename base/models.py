from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Many to one relation we use => models.ForeignKey
class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
# To delete task if user is delete we use models.CASCADE
# opposite of models.CASCADE is models.SET_NULL
    title = models.CharField(("Heading"), max_length=200, null=True, blank=True)
    description = models.TextField( null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField( auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']

    

