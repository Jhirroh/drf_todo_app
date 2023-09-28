from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ProfileViewSet, SignupAPIView, LoginAPIView, LogoutAPIView


router = DefaultRouter()
router.register('accounts/', ProfileViewSet, basename='profile')


urlpatterns = [
    path('signup/', SignupAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
]

urlpatterns += router.urls
