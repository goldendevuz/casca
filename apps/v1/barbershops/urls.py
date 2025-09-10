from django.urls import path

from apps.v1.barbershops.views import ServiceViewSet

urlpatterns = [
    path(
        "services/",
        ServiceViewSet.as_view({"get": "list"}),
        name="service-list"
    ),
]
