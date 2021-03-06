from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'articles', views.ArticleViesSet)

urlpatterns = [
    url(r'^', include(router.urls))
]