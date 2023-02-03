from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

from LuffyAPI.extension.mixins import ReListModelMixin, ReRetrieveModelMixin
from LuffyAPI.extension.page import ReLimitOffsetPagination, PageNumberPagination
from course import models
from serializers import course


class CourseFilterSet(FilterSet):
    """筛选"""
    # ?latest_id=3&limit=2（limit已在全局配置文件中配置）
    latest_id = filters.NumberFilter(field_name='id', lookup_expr='lte')
    # ?category=2
    category = filters.CharFilter(label='课程分类名称', field_name='course_category')

    class Meta:
        model = models.Course
        fields = ('latest_id', 'category')


class CourseCategoryView(GenericViewSet, ReListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = course.CourseCategoryModelSerializer


class CourseView(GenericViewSet, ReListModelMixin, ReRetrieveModelMixin):
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseFilterSet
    # 排序字段
    # ?ordering=-students
    ordering_fields = ('id', 'price', 'students')

    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = course.CourseModelSerializer


class CourseChapterView(GenericViewSet, ReListModelMixin, ReRetrieveModelMixin):
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('course',)

    queryset = models.CourseChapter.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = course.CourseChapterModelSerializer


class CourseSearchChapterView(GenericViewSet, ReListModelMixin):
    # http://127.0.0.1:8000/course/search/?search=linux
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = course.CourseModelSerializer
