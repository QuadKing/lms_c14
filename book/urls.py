from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter

from . import views

# router = SimpleRouter()
router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

# print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
    path('send_mail/', views.send_mail_function)
]
