from rest_framework.pagination import LimitOffsetPagination


class ReLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 100
    offset_query_param = None
