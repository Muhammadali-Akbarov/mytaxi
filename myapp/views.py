from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Client,Order,Driver
from .serializers import(
                            DriverSerializer,
                            ClientSerializer,
                            OrderSerializer,
                        )

@api_view(['GET','POST'])
def driversView(request):
    
    if request.method == "GET":      
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers,many=True,context={'request':request})
        
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DriverSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    

@api_view(['GET','PUT','DELETE'])
def driverDetailView(request,pk):
    
    driver = get_object_or_404(Driver,id=pk)
    
    if request.method == "GET":
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = DriverSerializer(driver,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
def clientsView(request):
    
    if request.method == "GET":      
        clients = Client.objects.all()
        serializer = ClientSerializer(clients,many=True,context={'request':request})
        
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def clientDetailView(request,pk):
    
    client = get_object_or_404(Client,id=pk)
    
    if request.method == "GET":
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ClientSerializer(client,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def ordersView(request):
    
    if request.method == "GET":      
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True,context={'request':request})
        
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def orderDetailView(request,order_pk,client_pk):
    
    try:
        order_item = Order.objects.get(id=order_pk)
        client_item = Client.objects.get(id=client_pk)
        order = Order.objects.get(id=order_pk)
    
        match_a =order_item.client.id
        match_b =client_item.id
        
        if request.method == "GET" and match_a==match_b:
            serializer = OrderSerializer(order)
            return Response(serializer.data)
            
        elif request.method == "PUT":
            serializer = OrderSerializer(order,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
                        
            return Response(serializer.data)
                    
        elif request.method == "DELETE":
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
                
        else:
            return Response({"error": "Content not found"}, status=status.HTTP_204_NO_CONTENT)
    
    except:
        return Response({"error": "Content not found"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def orderDetailDateView(request,driver_id,client_pk,gte_date,lte_date):
    
    if request.method == "GET":
        result = Order.objects.filter(client_id=client_pk,driver_id=driver_id,created_day__date__range=(gte_date,lte_date))
        serializer = OrderSerializer(result,many=True,context={'request':request})
        
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    else:
        return Response({"error": "Content not found"}, status=status.HTTP_204_NO_CONTENT)