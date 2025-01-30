from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def cart(request, item_id):
    return HttpResponse(f"This is the cart page. The item id is {item_id}")