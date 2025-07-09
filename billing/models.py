from django.db import models

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    invoice_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.customer_name}"

    def total_amount(self):
        return sum(item.total for item in self.items.all())


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    description = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} - ₹{self.total}"
