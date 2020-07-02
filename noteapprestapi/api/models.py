from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Note(models.Model):
    #choices for note_type
    NEW = 'NEW'
    READY = 'RDY'
    IN_PROGRESS = 'WIP'
    READY_FOR_TEST = 'TEST'
    DONE = 'DONE'
    TYPE_CHOICES = [
        (NEW, 'New'),
        (READY, 'Ready'),
        (IN_PROGRESS, 'In Progress'),
        (READY_FOR_TEST, 'Ready for test'),
        (DONE, 'Done')
    ]

    #object properties
    creation_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    note = models.TextField()
    is_task = models.NullBooleanField(default=False)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('tag')
    attachment = models.FileField(upload_to='uploads/')
    note_type = models.CharField(
        max_length=4, choices=TYPE_CHOICES, default=NEW)

    def __str__(self):
        return str(self.creation_date)
