from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 200


class SecondDefaultPagination(PageNumberPagination):
    page_size = 100
