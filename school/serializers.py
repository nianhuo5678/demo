# -*- encoding: utf-8 -*-
from rest_framework import serializers
from models import Student, Lesson, Score


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'name',
        )


class StudentSerializer(serializers.ModelSerializer):
    scores = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Student
        fields = (
            'id',
            'name',
            'scores',
        )

    def get_scores(self, obj):
        # l_id = self.context.get('request').GET['lesson_id']
        l_id = self.context.get('request').query_params['lesson_id']
        return Score.objects.get(student_id=obj.id, lesson_id=l_id).score


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'name',
        )


class ScoreSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    lesson_name = serializers.SerializerMethodField()

    class Meta:
        model = Score
        fields = (
            'student_id',
            'student_name',
            'lesson_id',
            'lesson_name',
            'score',
        )

    def get_student_name(self, obj):
        return obj.student_id.name

    def get_lesson_name(self, obj):
        return obj.lesson_id.name