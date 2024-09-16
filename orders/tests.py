from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer, Order

# class CustomerOrderAPITestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='testpass')
#         self.client.force_authenticate(user=self.user)
        
#         self.customer_data = {'name': 'John Doe', 'code': 'JD001', 'phone_number': '+254712345678'}
#         self.customer = Customer.objects.create(**self.customer_data)
        
#         self.order_data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': '100.00'}

#     def test_create_customer(self):
#         response = self.client.post('/api/customers/', self.customer_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Customer.objects.count(), 2)

#     def test_create_order(self):
#         response = self.client.post('/api/orders/', self.order_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Order.objects.count(), 1)

#     def test_get_customers(self):
#         response = self.client.get('/api/customers/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

#     def test_get_orders(self):
#         Order.objects.create(**self.order_data)
#         response = self.client.get('/api/orders/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)


class CustomerOrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        
        self.customer_data = {'name': 'John Doe', 'code': 'JD001', 'phone_number': '+254712345678'}
        self.customer = Customer.objects.create(**self.customer_data)
        
        self.order_data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': '100.00'}

    def test_create_customer(self):
        new_customer_data = {
            'name': 'Jane Doe', 
            'code': 'JD002',
            'phone_number': '+254787654321'
        }
        response = self.client.post('/api/customers/', new_customer_data, format='json')
        if response.status_code != status.HTTP_201_CREATED:
            print(f"Response status code: {response.status_code}")
            print(f"Response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)

    def test_create_order(self):
        response = self.client.post('/api/orders/', self.order_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_get_customers(self):
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_orders(self):
        Order.objects.create(customer=self.customer, item='Test Item', amount='100.00')
        response = self.client.get('/api/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
