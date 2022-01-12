from django.urls import path

from .views import(                   
                    driverDetailView, 
                    driversView,
                    
                    clientsView,
                    clientDetailView,
                    orderDetailDateView,
                    
                    ordersView,
                    orderDetailView,
                )


urlpatterns = [
    
    path('drivers/',driversView,name='drivers'),
    path('drivers/<str:pk>/',driverDetailView,name='driver-detail'),
    
    path('clients/',clientsView,name='clients'),
    path('clients/<str:pk>/',clientDetailView,name='client-detail'),
    
    path('orders/',ordersView,name='orders'),
    path('orders/<str:order_pk>/clients/<str:client_pk>/',orderDetailView,name='order-detail'),
    
    #addational
    path('orders/<str:driver_id>/clients/<str:client_pk>/from/<str:gte_date>/to/<str:lte_date>/',orderDetailDateView,name='order-datail-date-view')
    
]
