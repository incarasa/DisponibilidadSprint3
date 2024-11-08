from django.urls import path
from .views import PagoListView
from manejador_usuarios import views

urlpatterns = [
    path("pagos/", PagoListView.as_view(), name='pagos-list'),
    path('health/', views.health_check, name='health'),
]