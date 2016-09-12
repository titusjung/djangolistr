from django.db import models

# Create your models here.
class Entry(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey('auth.User')
    description = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "entries"