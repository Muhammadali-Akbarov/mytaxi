from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):

    routes = [
        
        {
            'Endpoint': '/api/v2/drivers/',
            'method': ['GET','POST'],
  
            'description': 'Returns an array of drivers'
        },
        {
            'Endpoint': '/api/v2/drivers/id',
            'method': ['GET','PUT','DELETE'],
            'description': 'Returns a single driver object'
        },
        
        {
            'Endpoint': '/api/v2/clients/',
            'method': ['GET','POST'],
            'description': 'Returns an array of clients'
        },
        {
            'Endpoint': '/api/v2/orders/',
            'method': ['GET','POST'],
            'description': 'Returns an array of orders'
        },
        {
            'Endpoint': '/api/v2/orders/order_id/clients/client_id',
            'method': ['GET','PUT','DELETE'],
            'description': 'Returns a single client object'
        },
        {
            'Endpoint': '/api/v2/orders/<str:driver_id>/clients/<str:client_pk>/from/<str:gte_date>/to/<str:lte_date>/',
            'method': ['GET'],
            'description': 'Returns an array of orders filtered with client,driver and from date to date'
        },
    ]
    return Response(routes)
