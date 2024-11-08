from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pago
from .serializers import PagoSerializer

class PagoListView(APIView):
    def get(self, request):
        estudiantes = Pago.objects.all()
        serializer = PagoSerializer(estudiantes, many=True)
        return Response(serializer.data)