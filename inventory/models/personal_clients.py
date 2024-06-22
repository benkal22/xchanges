from django.db import models
from inventory.models.producers import Producer

#PersonalClient
class PersonalClient(models.Model):
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_personal_client')
    personal_client_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
