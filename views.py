from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import APIView
from .models import Invoice_detail,uploader
from rest_framework.response import Response
from.serializer import InvoiceSerializer,UploderSerializer,StatusSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class InvoiceCR(ModelViewSet):
    queryset = Invoice_detail.objects.all()
    serializer_class = InvoiceSerializer

class UploaderCR(ModelViewSet):
    queryset = uploader.objects.all()
    serializer_class = UploderSerializer

class StatusView(APIView):
    def get(self,request,pid):
        product = get_object_or_404(Invoice_detail, pk=pid)
        serializer=StatusSerializer(product)
        return Response(serializer.data)