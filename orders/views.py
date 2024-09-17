from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

# Create your views here.
from rest_framework import viewsets,status
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from .utils import send_sms
from mozilla_django_oidc.utils import import_from_settings
from django.contrib.auth import logout
from django.shortcuts import redirect


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_root(request):

    """
    API root endpoint.
    """

    user = request.user
    session_data = {key: str(value) for key, value in request.session.items()}
    return Response({
        "message": "Welcome to the Customer Order Service API",
        "user": user.username,
        "authenticated": user.is_authenticated
    })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """
    Logout the current user.
    """
    if request.method == 'GET':
        return Response({"message": "Please use POST to logout."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    logout(request)
    oidc_logout_url = import_from_settings('OIDC_OP_LOGOUT_ENDPOINT', '')
    if oidc_logout_url:
        return redirect(oidc_logout_url)
    return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)

class CustomerViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows customers to be viewed or edited.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class OrderViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows orders to be viewed or edited.
    """
        
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        send_sms(order.customer.phone_number, f"Hello {order.customer.name}\nYour new order has been received:\nOrder ID - {order.id} \nItem - {order.item} \nAmount- Kshs. {order.amount} ")

