from django.db import models

# 1. โมเดลสำหรับสินค้า (Product)
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True)

    def __str__(self):
        return self.name


# 2. โมเดลสำหรับเก็บข้อมูลการสั่งซื้อและที่อยู่จัดส่ง (Order)
class Order(models.Model):
    # ข้อมูลลูกค้า
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    date_ordered = models.DateTimeField(auto_now_add=True)

    # ข้อมูลการขนส่ง (ที่เพิ่มใหม่)
    shipping_method = models.CharField(max_length=100, default='Standard')
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.full_name}"