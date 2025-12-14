from django.db import models

class Stock(models.Model):
    # Header fields
    date = models.DateField()
    remark = models.CharField(max_length=255)
    currency = models.CharField(max_length=10)
    project = models.CharField(max_length=100)

    # Body fields
    item_code = models.CharField(max_length=50)
    item_description = models.TextField()
    warehouse = models.CharField(max_length=100)
    quantity_issued = models.PositiveIntegerField()
    stock_balance = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()

    def __str__(self):
        return self.item_description
