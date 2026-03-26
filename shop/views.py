from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Product, Order

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    return render(request, 'shop/product_list.html', {'products': products, 'cart_count': sum(cart.values())})

def cart_add(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    cart[p_id] = cart.get(p_id, 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def cart_remove(request, product_id):
    cart = request.session.get('cart', {})
    p_id = str(product_id)
    if p_id in cart: del cart[p_id]
    request.session['cart'] = cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for p_id, qty in cart.items():
        product = get_object_or_404(Product, id=p_id)
        subtotal = product.price * qty
        total_price += subtotal
        cart_items.append({'product': product, 'quantity': qty, 'subtotal': subtotal})
    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart: return redirect('product_list')
    total_price = sum(get_object_or_404(Product, id=p_id).price * qty for p_id, qty in cart.items())

    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        payment = request.POST.get('payment_method')
        Order.objects.create(
            user=request.user,
            fullname=fullname,
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            total_price=total_price,
            payment_method=payment,
            slip_image=request.FILES.get('slip_image')
        )
        request.session['cart'] = {}
        return render(request, 'shop/success.html', {'fullname': fullname, 'payment': payment})
    return render(request, 'shop/checkout.html', {'total_price': total_price})

def login_user(request):
    if request.method == 'POST':
        u, p = request.POST.get('username'), request.POST.get('password')
        user = authenticate(request, username=u, password=p)
        if user:
            login(request, user)
            return redirect('product_list')
    return render(request, 'shop/login.html')

def logout_user(request):
    logout(request)
    return redirect('product_list')