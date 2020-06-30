from rest_framework import serializers

from .models import Student_subject_mapping, Student


class StudentSubjectMappingSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.subject.id

    def get_name(self, obj):
        return obj.subject.name

    class Meta:
        model = Student_subject_mapping
        fields = ['id', 'name']


class StudentSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    def get_subjects(self, obj):
        return StudentSubjectMappingSerializer(obj.all(), many=True).data

    class Meta:
        model = Student
        fields = ['id', 'email', 'subjects']