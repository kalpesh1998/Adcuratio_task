from django.db import models
from .validator import validate_file_extension

# Create your models here.
STATUS = (
    (0,"Pending"),
    (1,"Completed")
)

class Invoice_detail(models.Model):
    invoice_number=models.TextField(blank=True,null=True,max_length=15)
    invoice_date=models.DateField()
    seller=models.TextField(blank=True,null=True,max_length=40)
    seller_add=models.TextField(blank=True,null=True,max_length=100)
    buyer_name=models.CharField(blank=True,null=True,max_length=32)
    buyer_mobile=models.IntegerField()
    items=models.TextField(null=True,blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.invoice_number


class uploader(models.Model):
    file=models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_file_extension])
