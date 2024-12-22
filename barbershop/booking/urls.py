from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'masters', MasterViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'schedules', ScheduleViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
