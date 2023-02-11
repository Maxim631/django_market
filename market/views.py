from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseNotFound

import users.models
from .models import Product, Order, Ticket
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import F



class ShowProducts(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'products.html', {'products': products})


def main(request):
    return render(request, "main.html", {"username": request.user.username})


class ShowProduct(View):
    def get(self, request, product_id):
        product: Product = get_object_or_404(Product, id=product_id)
        return render(request, "product.html",{"product": product})


@method_decorator(login_required, name='dispatch')
class NewOrder(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request, "new_order.html", {"product": product})


    def post(self, request):
            order = Order()
            product = Product()
            order.count = request.POST.get("count")
            order.products_id = request.POST.get("products")
            order.user = request.user
            if order.count:
                product = Product.objects.get(id=order.products_id)
                Product.objects.filter(id=order.products_id).update(count=F('count') - order.count)
                order_cost = int(order.count) * int(product.cost)
                users.models.User.objects.filter(username=order.user).update(points=F('points') - order_cost)
                order.save()
                return redirect("/products")
            # return render(request, "new_order.html", {"product": product})

@method_decorator(login_required, name='dispatch')
class EditOrder(View):
    def get(self, request, order_id):
        products = Product.objects.all()
        order = Order.objects.get(id=order_id)

        return render(request, "edit_order.html", {"order": order, "products":products})

    def post(self, request, order_id):
            order = Order.objects.get(id=order_id)
            products = Product.objects.all()

            order.products_id = request.POST.get("products")
            order.count = request.POST.get("count")

            if order.count and order.products_id:

                order.save()
                return redirect("/profile", order_id)
            return render(request, "edit_order.html", {"order": order, "products": products})


@method_decorator(login_required, name="dispatch")
class AddPoints(View):
    def get(self, request):
        tickets = Ticket.objects.all()
        return render(request, "tickets.html", {"tickets": tickets})

    def post(self, request):
        uuid = request.POST.get('uuid')
        available = request.POST.get('available')
        user = request.user
        ticket = Ticket.objects.get(uuid=uuid)
        if ticket.available == 1:
            Ticket.objects.filter(uuid=uuid).update(available=False)
            users.models.User.objects.filter(username=user).update(points=F('points') + 100)
            return redirect("/")
        return render(request, "tickets.html")


@method_decorator(login_required, name='dispatch')
class ShowProfile(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, "profile.html", {"orders": orders})


@method_decorator(login_required, name='dispatch')
class DeleteOrder(View):
    def post(self, request, order_id: int):
        Order.objects.filter(id=order_id).delete()
        return redirect("/profile")













