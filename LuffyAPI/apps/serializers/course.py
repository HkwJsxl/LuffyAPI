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


class CourseSectionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CourseSection
        fields = (
            'id',
            'name',
            'ordering',
            'section_link',
            'duration',
            'publish_date',
            'free_trail',

            'section_type_name',
        )


class CourseChapterModelSerializer(serializers.ModelSerializer):
    """
    course_sections = CourseSectionModelSerializer()
    报错：
    AttributeError: Got AttributeError when attempting to get a value for field `ordering` on serializer `CourseSectionModelSerializer`.
    The serializer field might be named incorrectly and not match any attribute or key on the `RelatedManager` instance.
    Original exception text was: 'RelatedManager' object has no attribute 'ordering'.
    """
    # 一定要加many=True（一个章节有多个课时）
    course_sections = CourseSectionModelSerializer(many=True)

    class Meta:
        model = models.CourseChapter
        fields = (
            'id',
            'name',
            'chapter',
            'summary',
            'publish_date',

            'course',
            'course_sections',
        )
