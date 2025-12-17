from django.db import models

class Sales(models.Model):
    # Header fields
    date = models.DateField()
    client_name = models.CharField(max_length=255)
    client_code = models.CharField(max_length=50)
    client_address = models.TextField()
    project_name = models.CharField(max_length=255)
    warehouse = models.CharField(max_length=255)

    # Body fields
    item_id = models.CharField(max_length=50)
    item_code = models.CharField(max_length=50)
    item_description = models.TextField()
    quantity_sold = models.PositiveIntegerField()
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Sales {self.item_code} - {self.client_name}"

