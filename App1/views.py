from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')    
def profile(request):
    return render(request,'profile.html')
def orders(request):
    return render(request,'orders.html')
def cart(request):
    return render(request,'cart.html')
def categories(request):
    return render(request,'categories.html')
def fastrack(request):
    return render(request,'fastrack.html')
def sonata(request):
    return render(request,'sonata.html')
def titan(request):
    return render(request,'titan.html')
def kenneth(request):
    return render(request,'kenneth.html')
def anne(request):
    return render(request,'anne.html')
def edge(request):
    return render(request,'edge.html')
def nebula(request):
    return render(request,'nebula.html')
def maritime(request):
    return render(request,'maritime.html')
def men(request):
    return render(request,'men.html')
def women(request):
    return render(request,'women.html')
def cart(request):
    return render(request,'cart.html')
def add_to_cart(request):
  if request.method == 'POST':
    product_name = request.POST.get('product_name')
    price = request.POST.get('price')
    # Validate and sanitize data if needed

    # Create a new CartItem object
    cart_item = CartItem.objects.create(
        product_name=product_name, price=price
    )

    return JsonResponse({'message': 'Product added to cart'})
  else:
    return JsonResponse({'error': 'Invalid request method'})
  
def get_cart_items(request):
    cart_items = CartItem.objects.all().order_by('-id')  # Get latest items first
    data = [{'product_name': item.product_name, 'price': item.price} for item in cart_items]
    return JsonResponse(data)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             