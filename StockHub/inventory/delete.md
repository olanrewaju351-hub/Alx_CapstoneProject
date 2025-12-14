# Delete Stock

```python
stock = Stock.objects.get(item_code="ST001")
stock.delete()

Stock.objects.all()
