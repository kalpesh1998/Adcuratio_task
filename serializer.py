from .models import Invoice_detail,uploader
from rest_framework.serializers import ModelSerializer
class InvoiceSerializer(ModelSerializer):
    class Meta:
        model=Invoice_detail
        fields='__all__'

class UploderSerializer(ModelSerializer):
    class Meta:
        model=uploader
        fields='__all__'

class StatusSerializer(ModelSerializer):
    class Meta:
        model=Invoice_detail
        fields=['status','id']