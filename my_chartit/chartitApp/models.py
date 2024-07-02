# models.py
from django.db import models

class SalesReport(models.Model):
    month = models.IntegerField()  # Assuming month is stored as an integer
    sales = models.DecimalField(max_digits=10, decimal_places=2)  # Use DecimalField for monetary values

    @property
    def month_name(self):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
                 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names.get(self.month, 'Unknown')

    def __str__(self):
        return f"{self.month_name}: {self.sales}"


    @property
    def get_month_name(self):
        return self.month_name()

    @classmethod
    def get_sales_data(cls):
        queryset = cls.objects.all()
        data = [{'month_name': entry.month_name(), 'sales': entry.sales} for entry in queryset]
        return data
# models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
