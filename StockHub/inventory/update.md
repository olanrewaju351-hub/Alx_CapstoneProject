# Update Stock

```python
stock = Stock.objects.get(item_code="ST001")
stock.stock_balance = 40
stock.remarks = "Stock updated after issuance"
stock.save()
