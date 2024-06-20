from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from inventory.models import Product

class ProductAPITestCase(APITestCase):

    def setUp(self):
        # Create initial test data
        self.product1 = Product.objects.create(
            sector_code='S',
            sector_label='AUTRES ACTIVITÉS DE SERVICES N.C.A.',
            activity_code='S940200',
            activity_label='Activités des syndicats des travailleurs',
            product_code='S94020000',
            product_label='Services fournis par les syndicats de travailleurs'
        )
        self.product2 = Product.objects.create(
            sector_code='A',
            sector_label='Agriculture',
            activity_code='A011',
            activity_label='Crop production',
            product_code='A0110000',
            product_label='Crop products'
        )
        self.valid_payload = {
            'sector_code': 'B',
            'sector_label': 'Construction',
            'activity_code': 'B012',
            'activity_label': 'Building construction',
            'product_code': 'B0120000',
            'product_label': 'Building products'
        }
        self.invalid_payload = {
            'sector_code': '',
            'sector_label': 'Invalid',
            'activity_code': 'B012',
            'activity_label': 'Building construction',
            'product_code': 'B0120000',
            'product_label': 'Building products'
        }

    def test_create_valid_product(self):
        url = reverse('products-list')
        response = self.client.post(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        url = reverse('products-list')
        response = self.client.post(url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_products(self):
        url = reverse('products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_product_by_id(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['product_code'], self.product1.product_code)

    def test_update_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.id})
        update_payload = {
            'sector_code': 'S',
            'sector_label': 'AUTRES ACTIVITÉS DE SERVICES N.C.A. UPDATED',
            'activity_code': 'S940200',
            'activity_label': 'Activités des syndicats des travailleurs',
            'product_code': 'S94020000',
            'product_label': 'Services fournis par les syndicats de travailleurs'
        }
        response = self.client.put(url, data=update_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.sector_label, 'AUTRES ACTIVITÉS DE SERVICES N.C.A. UPDATED')

    def test_partial_update_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.id})
        partial_update_payload = {'sector_label': 'Updated Label'}
        response = self.client.patch(url, data=partial_update_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.sector_label, 'Updated Label')

    def test_delete_product(self):
        url = reverse('products-detail', kwargs={'pk': self.product1.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product1.id).exists())

    def test_get_non_existent_product(self):
        url = reverse('products-detail', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_non_existent_product(self):
        url = reverse('products-detail', kwargs={'pk': 9999})
        response = self.client.put(url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_non_existent_product(self):
        url = reverse('products-detail', kwargs={'pk': 9999})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
