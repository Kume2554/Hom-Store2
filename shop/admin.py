from django.contrib import admin
from .models import Product

# ลงทะเบียน Model Product ให้ขึ้นในหน้า Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # กำหนดให้หน้า List โชว์คอลัมน์อะไรบ้าง (ดูง่ายขึ้นเยอะ)
    list_display = ('name', 'price', 'image')
    # เพิ่มช่องค้นหาชื่อสินค้า
    search_fields = ('name',)