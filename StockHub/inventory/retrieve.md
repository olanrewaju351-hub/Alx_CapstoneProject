# Retrieve Stock

```python
stock = Stock.objects.get(item_code="ST001")
print(
    stock.date,
    stock.remark,
    stock.currency,
    stock.project,
    stock.item_code,
    stock.item_description,
    stock.warehouse,
    stock.quantity_issued,
    stock.stock_balance,
    stock.price,
    stock.remarks
)

