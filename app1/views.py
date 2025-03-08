from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db.models import Q
# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from app1.models import *
# Create your views here.


def base(request):
    return render(request,'base.html')


def input_data(request):
    if request.method=="POST":
        product_id=request.POST['product_id']
        invoice=request.POST["invoice"]
        receiver_name=request.POST["receiver_name"]
        booking_date=request.POST["booking_date"]
        delivery_date=request.POST["delivery_date"]
        description=request.POST["description"]
        quantity=request.POST["quantity"]
        to_pay=request.POST["to_pay"]
        place=request.POST["place"]
        consignee_person=request.POST["consignee_person"]
        vehicle_number=request.POST["vehicle_number"]
        PO=Product.objects.get_or_create(product_id=product_id,invoice=invoice,receiver_name=receiver_name,booking_date=booking_date,delivery_date=delivery_date,description=description,quantity=quantity,to_pay=to_pay,place=place,consignee_person=consignee_person,vehicle_number=vehicle_number)
        # if(PO):
        #     return HttpResponse(f'{receiver_name} is created sussfully')
        # else:
        #     return HttpResponse(f'{receiver_name} is already created')
    return render(request,'index.html')

def get_output(request):
    PO=Product.objects.all()
    d={"PO":PO}
    return render(request,'output.html',d)


def products_data_fetch(request):
    search_query = request.GET.get('search', '')

    # Filter data based on search query or fetch all
    if search_query:
        PO = Product.objects.filter(Q(product_id__icontains=search_query) | Q(description__icontains=search_query))
    else:
        PO = Product.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        
        try:
            product = Product.objects.get(product_id=product_id)
            
            if action == 'update':
                product.invoice = request.POST.get('invoice')
                product.receiver_name = request.POST.get('receiver_name')
                product.booking_date = request.POST.get('booking_date')
                product.delivery_date = request.POST.get('delivery_date')
                product.description = request.POST.get('description')
                product.quantity = request.POST.get('quantity')
                product.to_pay = request.POST.get('to_pay')
                product.place = request.POST.get('place')
                product.consignee_person = request.POST.get('consignee_person')
                product.vehicle_number = request.POST.get('vehicle_number')
                product.save()
            
            elif action == 'delete':
                product.delete()

        except Product.DoesNotExist:
            pass

        return redirect('products_data_fetch')

    return render(request, 'output.html', {'PO': PO, 'search_query': search_query})


