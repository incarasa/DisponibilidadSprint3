from django.urls import path
from .views import PagoListView

urlpatterns = [
    path("pagos/", PagoListView.as_view(), name='pagos-list'),
]