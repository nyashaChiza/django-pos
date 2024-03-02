from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .models import Customer


# TODO: Remove duplicate code


@login_required(login_url="/accounts/login/")
def customers_list_view(request: HttpRequest) -> HttpResponse:
    context = {"active_icon": "customers", "customers": Customer.objects.all()}
    return render(request, "customers/customers.html", context=context)


@login_required(login_url="/accounts/login/")
def customers_add_view(request: HttpRequest) -> HttpResponse:
    context = {
        "active_icon": "customers",
    }

    if request.method == "POST":
        # Save the POST arguments
        data = request.POST

        attributes = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "address": data["address"],
            "email": data["email"],
            "phone": data["phone"],
            "kra_pin": data["kra_pin"],
        }

        # Check if a customer with the same attributes exists
        if Customer.objects.filter(**attributes).exists():
            messages.error(request, "Customer already exists!", extra_tags="warning")
            return redirect("customers:customers_add")

        try:
            # Create the customer
            new_customer = Customer.objects.create(**attributes)

            # If it doesn't exist, save it
            new_customer.save()

            messages.success(
                request,
                f'Customer: {attributes["first_name"]} {attributes["last_name"]}  created '
                f"successfully!",
                extra_tags="success",
            )
            return redirect("customers:customers_list")
        except Exception as e:
            messages.success(
                request, "There was an error during the creation!", extra_tags="danger"
            )

            return redirect("customers:customers_add")

    return render(request, "customers/customers_add.html", context=context, status=200)


@login_required(login_url="/accounts/login/")
def customers_update_view(request: HttpRequest, customer_id: str) -> HttpResponse:
    """
    Args:
        request: HttpRequest Object
        customer_id : The customer's ID that will be updated
    """

    # Get the customer
    try:
        # Get the customer to update
        customer = Customer.objects.get(id=customer_id)
    except Exception as e:
        messages.success(
            request,
            "There was an error trying to get that customer!",
            extra_tags="danger",
        )

        return redirect("customers:customers_list")

    context = {
        "active_icon": "customers",
        "customer": customer,
    }

    if request.method == "POST":
        try:
            # Save the POST arguments
            data = request.POST

            attributes = {
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "address": data["address"],
                "email": data["email"],
                "phone": data["phone"],
                "kra_pin": data["kra_pin"],
            }

            # Check if a customer with the same attributes exists
            if Customer.objects.filter(**attributes).exists():
                messages.error(
                    request, "Customer already exists!", extra_tags="warning"
                )
                return redirect("customers:customers_add")

            # Get the customer to update
            Customer.objects.filter(id=customer_id).update(**attributes)

            customer = Customer.objects.get(id=customer_id)

            messages.success(
                request,
                "¡Customer: " + customer.get_full_name() + " updated successfully!",
                extra_tags="success",
            )
            return redirect("customers:customers_list")
        except Exception as e:
            messages.success(
                request, "There was an error during the update!", extra_tags="danger"
            )

            return redirect("customers:customers_list")

    return render(request, "customers/customers_update.html", context=context)


@login_required(login_url="/accounts/login/")
def customers_delete_view(request: HttpRequest, customer_id: str) -> HttpResponse:
    """
    Args:
        request: HttpRequest Object
        customer_id : The customer's ID that will be deleted
    """
    try:
        # Get the customer to delete
        customer = Customer.objects.get(id=customer_id)
        customer.delete()
        messages.success(
            request,
            "¡Customer: " + customer.get_full_name() + " deleted!",
            extra_tags="success",
        )
        return redirect("customers:customers_list")
    except Exception as e:
        messages.success(
            request,
            "There was an error deleting that customer, may be the customer has an existing sale record",
            extra_tags="danger",
        )

        return redirect("customers:customers_list")
