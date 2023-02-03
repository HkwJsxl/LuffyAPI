from rest_framework import serializers

from course import models


class CourseCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ('id', 'name',)


class TeacherModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = (
            'id',
            'name',
            'title',
            'signature',
            'image',
            'brief',

            'role_name',
        )


class CourseModelSerializer(serializers.ModelSerializer):
    teacher = TeacherModelSerializer()

    class Meta:
        model = models.Course
        fields = (
            'id',
            'name',
            'price',
            'course_image',
            'brief',
            'publish_date',
            'period',
            'attachment_path',
            'students',
            'sections',
            'publish_sections',

            'course_type_name',
            'level_name',
            'status_name',

            'course_category_name',
            'teacher',
            'course_section',
        )
