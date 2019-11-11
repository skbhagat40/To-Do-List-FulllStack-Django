from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class ItemsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('priority')


class BroadTopics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)


class SubTopics(models.Model):
    title = models.CharField(max_length=1000)
    broadTopic = models.ForeignKey(BroadTopics, blank=True, null=True, on_delete=models.SET_NULL,
                                   related_name='subtopics')
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Items(models.Model):
    description = models.TextField()
    subTopic = models.ForeignKey(SubTopics, blank=True, null=True, on_delete=models.SET_NULL, related_name='items')
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    objects = ItemsManager()
