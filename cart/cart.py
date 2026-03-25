from decimal import Decimal
from shop.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id in self.cart:
            if 'qty' in self.cart[product_id]:
                self.cart[product_id]['qty'] += int(quantity)
            else:
                self.cart[product_id]['qty'] = int(quantity)
                self.cart[product_id]['price'] = str(product.price)
        else:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(quantity)}
        self.session.modified = True

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    # ---- เพิ่มใหม่: ฟังก์ชันอัปเดตจำนวนสินค้า ----
    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = int(quantity) # แทนที่ด้วยจำนวนใหม่ที่ลูกค้าพิมพ์
        self.session.modified = True
    # ----------------------------------------

    def __len__(self):
        return sum(item.get('qty', 1) for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item.get('price', 0))
            item['qty'] = item.get('qty', 1)
            item['total_price'] = item['price'] * item['qty']
            yield item

    def get_total_price(self):
        return sum(Decimal(item.get('price', 0)) * item.get('qty', 1) for item in self.cart.values())