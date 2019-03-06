from django.db import models
from django.contrib import admin

# Create your models here.
class Issue(models.Model):
    TO_DO = 1
    IN_PROGRESS = 2
    CODE_REVIEW = 3
    REDO = 4
    TEST = 5
    DONE = 6
    STATUS_CHOICES = (
        (TO_DO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (CODE_REVIEW, 'Code Review'),
        (REDO, 'Redo'),
        (TEST, 'Test'),
        (DONE, 'Done'),
    )

    BUG = 3
    STORY = 1
    TASK = 2
    SUB_TASK = 4
    KIND_CHOICES = (
        (STORY, 'Story'),
        (TASK, 'Task'),
        (BUG, 'Bug'),
        (SUB_TASK, 'Sub-Task')
    )
    thesnr = models.CharField(max_length=200, default="THES-")
    description = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=TO_DO)
    kind = models.IntegerField(choices=KIND_CHOICES, default=BUG)
    sprint = models.IntegerField(default=5)

    def __str__(self):
        return self.thesnr



