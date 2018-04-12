# -*- encoding: utf-8 -*-
from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ('id',)
        db_table = 'student'

    def __str__(self):
        return self.name

class Lesson(models.Model):
    id = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ('id',)
        db_table = 'lesson'

    def __str__(self):
        return self.name

class Score(models.Model):
    student_id = models.ForeignKey(Student, null=True, related_name='student_id')
    lesson_id = models.ForeignKey(Lesson, null=True, related_name='lesson_id')
    score = models.IntegerField(null=False)

    class Meta:
        db_table = 'score'

    def __str__(self):
        return '%s, %s, %d' % (self.score_id.name, self.student_id.name, self.score)