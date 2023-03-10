from django.urls import include, path
from rest_framework import routers

from .views import BarViewSet, DrinkViewSet, LanguageViewSet, ThemeViewSet

app_name = 'api'

router = routers.DefaultRouter()

router.register(r'bars', BarViewSet, basename='bars')
router.register(r'drinks', DrinkViewSet, basename='drinks')
router.register(r'languages', LanguageViewSet, basename='languages')
router.register(r'themes', ThemeViewSet, basename='themes')

urlpatterns = [
    path('', include(router.urls)),
]
