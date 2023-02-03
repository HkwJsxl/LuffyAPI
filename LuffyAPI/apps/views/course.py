from rest_framework.viewsets import GenericViewSet
from rest_framework.filters import OrderingFilter

from django_filters import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend

from LuffyAPI.extension.response import APIResponse
from LuffyAPI.extension.mixins import ReListModelMixin
from LuffyAPI.extension.page import ReLimitOffsetPagination
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


class CourseView(GenericViewSet, ReListModelMixin):
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CourseFilterSet
    # 排序字段
    # ?ordering=-students
    ordering_fields = ('id', 'price', 'students')

    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = course.CourseModelSerializer
