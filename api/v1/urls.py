from django.urls import path

from .views import CreateUserView, VerifyAPIView, GetNewVerification, \
    UpdateUserInformationView, ChangeUserPhotoView, LoginView, LoginRefreshView, \
    LogOutView, ResetPasswordView, PasswordGeneratorView, test_login, ForgetPasswordAPIView, ProfileDetailUpdateView

user_urlpatterns = [
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='refresh'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetNewVerification.as_view(), name='new-verify'),
    path('', UpdateUserInformationView.as_view(), name='update'),
    path('photo/', ChangeUserPhotoView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget-password'),
    path('test-login/', test_login, name='test-login'),
    path('generate-password/', PasswordGeneratorView.as_view(), name='generate-password'),
    path('profile/', ProfileDetailUpdateView.as_view(), name='profile-detail-update'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.v1.system.views import NotificationViewSet, NotificationSettingViewSet, PaymentViewSet

system_router = DefaultRouter()
system_router.register(r'notifications', NotificationViewSet, basename='notification')
system_router.register(r'notification-settings', NotificationSettingViewSet, basename='notification-setting')
system_router.register(r'payments', PaymentViewSet, basename='payment')

barbershop_router = DefaultRouter()
barbershop_router.register(r'', BarbershopViewSet)
barbershop_router.register(r'specialties', SpecialtyViewSet)
barbershop_router.register(r'services', ServiceViewSet)
barbershop_router.register(r'banners', BannerViewSet)
barbershop_router.register(r'contacts', ContactUsViewSet)

barber_router = DefaultRouter()
barber_router.register(r'', BarberViewSet, basename='barber')
barber_router.register(r'favorites', FavoriteViewSet, basename='favorite')
barber_router.register(r'histories', HistoryViewSet, basename='history')
barber_router.register(r'security-settings', SecuritySettingViewSet, basename='securitysetting')
barber_router.register(r'working-hours', WorkingHourViewSet, basename='workinghour')

appointment_router = DefaultRouter()
appointment_router.register('', AppointmentViewSet, basename='appointment')
appointment_router.register('reasons', ReasonViewSet, basename='reason')
appointment_router.register('reviews', ReviewViewSet, basename='review')
appointment_router.register('rates', RateViewSet, basename='rate')
appointment_router.register('review-likes', ReviewLikeViewSet, basename='reviewlike')

urlpatterns = [
    path('system', include(system_router.urls)),
    path('barbershop', include(barbershop_router.urls)),
    path('barber', include(barber_router.urls)),
    path('appointment', include(appointment_router.urls)),
]

urlpatterns = user_urlpatterns + system_router.urls + barbershop_router.urls + barber_router.urls + appointment_router.urls
