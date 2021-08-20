from django.db import models

# Create your models here.

class List(models.Model):
    class Meta():
        verbose_name_plural = "List"
    task = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task