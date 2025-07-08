from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from reservation_app.views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'menus', MenuViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
