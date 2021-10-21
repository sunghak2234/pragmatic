import os

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Question(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='question')
    title = models.CharField(max_length=200, null=True)
    image = models.FileField(upload_to='question/', null=True, blank=True)
    content = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    question_hit = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


    def get_file_name(self):
        return os.path.basename(self.image.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

    @property
    def test_123(self):
        self.question_hit += 1
        self.save()

