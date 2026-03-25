from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from shop.models import Product
from .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/cart_summary.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        return JsonResponse({'qty': cart.__len__()})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        return JsonResponse({'qty': cart.__len__(), 'total': cart.get_total_price()})

# ---- เพิ่มใหม่: ฟังก์ชันรับคำสั่งอัปเดตจำนวน ----
def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product=product_id, quantity=product_qty) # สั่งอัปเดตจำนวน
        
        return JsonResponse({'qty': cart.__len__(), 'total': cart.get_total_price()})
# ------------------------------------------

def checkout(request):
    return render(request, 'cart/checkout.html', {})