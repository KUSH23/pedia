from rest_framework import pagination

class MyAPIPagination(pagination.LimitOffsetPagination):
    # page_size = 6
    default_limit = 10
    max_limit = 7