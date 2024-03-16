import time
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
import json
from inventory.models import Inventory
from products.models import Product


# Create your views here.
def index(request):
    inventory = Inventory.objects.all()
    context = {"inventory": inventory, "active_icon": "inventory"}
    return render(request, "inventory/inventory.html", context)


def add_inventory(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        # only products that are not in the inventory
        products = Product.objects.exclude(inventory__isnull=False)
        return render(request, "inventory/inventory_add.html", {"products": products})
    elif request.method == "POST":
        data = json.loads(request.body)
        product_id = int(data["product"])
        quantity = int(data["quantity"])
        product = Product.objects.get(id=product_id)
        inventory = Inventory(product=product, quantity=quantity)
        try:
            inventory.save()
            return JsonResponse({"status": "success"}, safe=True)
        except Exception as ee:
            return JsonResponse({"status": "fail", "error": str(ee)}, safe=True)


def update_inventory(request: HttpRequest, inventory_id: int) -> HttpResponse:
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == "GET":
        return render(
            request, "inventory/inventory_update.html", {"inventory": inventory}
        )
    elif request.method == "POST":
        data = json.loads(request.body)
        quantity = int(data["quantity"])
        inventory.quantity = quantity
        inventory.save()
        return JsonResponse({"status": "success"}, safe=True)
