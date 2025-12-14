# Create Stock

```python
from inventory.models import Stock
from datetime import date

stock = Stock.objects.create(
    date=date.today(),
    remark="Initial stock record",
    currency="NGN",
    project="StockHub Inventory",
    item_code="ST001",
    item_description="Laptop",
    warehouse="Central Warehouse",
    quantity_issued=5,
    stock_balance=45,
    price=350000.00,
    remarks="Brand new stock"
)
