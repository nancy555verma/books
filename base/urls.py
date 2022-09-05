from . import views
from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import MarkBookModelViewSet

router = routers.SimpleRouter()
router.register(r'books', views.BookModelViewSet, basename='book')
# router.register(r'mark-book', views.markbookview, basename='mark-book')
urlpatterns = [
    path("login/", obtain_auth_token, name='obtain-auth-token'),
    path("mark-book/<str:pk>", MarkBookModelViewSet.as_view(), name='mark-book'),
]+router.urls