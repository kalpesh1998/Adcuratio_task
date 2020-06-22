from .views import InvoiceCR,UploaderCR

from django.urls import path,include
from rest_framework import routers

router = routers.SimpleRouter()



router.register(r'invoice',InvoiceCR)
router.register(r'uploader',UploaderCR)

urlpatterns = router.urls