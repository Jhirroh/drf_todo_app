from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TaskViewset

router = DefaultRouter()

router.register('', TaskViewset, basename='task')

urlpatterns = [

]

urlpatterns += router.urls
