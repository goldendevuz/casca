from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

# -----------------------------
# User endpoints (manual paths)
# -----------------------------
user_urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='refresh'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetNewVerification.as_view(), name='new-verify'),
    path('photo/', ChangeUserPhotoView.as_view(), name='change-photo'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget-password'),
    path('test-login/', test_login, name='test-login'),
    path('generate-password/', PasswordGeneratorView.as_view(), name='generate-password'),
    path('profile/', ProfileDetailUpdateView.as_view(), name='profile-detail-update'),
    path('', UpdateUserInformationView.as_view(), name='update'),
]

# -----------------------------
# Routers for viewsets
# -----------------------------
system_router = DefaultRouter()
system_router.register(r'notifications', NotificationViewSet, basename='notification')
system_router.register(r'notification-settings', NotificationSettingViewSet, basename='notification-setting')
system_router.register(r'payments', PaymentViewSet, basename='payment')

barbershop_router = DefaultRouter()
barbershop_router.register(r'specialties', SpecialtyViewSet)
barbershop_router.register(r'services', ServiceViewSet)
barbershop_router.register(r'banners', BannerViewSet)
barbershop_router.register(r'contacts', ContactUsViewSet)
barbershop_router.register(r'', BarbershopViewSet)

barber_router = DefaultRouter()
barber_router.register(r'favorites', FavoriteViewSet, basename='favorite')
barber_router.register(r'histories', HistoryViewSet, basename='history')
barber_router.register(r'security-settings', SecuritySettingViewSet, basename='securitysetting')
barber_router.register(r'working-hours', WorkingHourViewSet, basename='workinghour')
barber_router.register(r'', BarberViewSet, basename='barber')

appointment_router = DefaultRouter()
appointment_router.register('reasons', ReasonViewSet, basename='reason')
appointment_router.register('reviews', ReviewViewSet, basename='review')
appointment_router.register('rates', RateViewSet, basename='rate')
appointment_router.register('review-likes', ReviewLikeViewSet, basename='reviewlike')
appointment_router.register('', AppointmentViewSet, basename='appointment')

# -----------------------------
# Combine everything in urlpatterns
# -----------------------------
urlpatterns = [
    path('user/', include(user_urlpatterns)),  # user manual endpoints
    path('system/', include(system_router.urls)),
    path('barbershop/', include(barbershop_router.urls)),
    path('barber/', include(barber_router.urls)),
    path('appointment/', include(appointment_router.urls)),
]
