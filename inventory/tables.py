# inventory/tables.py
import django_tables2 as tables
from inventory.models import CompanyClient, Supplier

class CompanyClientTable(tables.Table):
    actions = tables.TemplateColumn(template_name='inventory/clients_table_actions.html')

    class Meta:
        model = CompanyClient
        fields = ('company_name', 'email',)  # Champs à afficher dans le tableau
        template_name = 'django_tables2/bootstrap4.html'  # Template pour le style

# class SupplierTable(tables.Table):
#     class Meta:
#         model = Supplier
#         template_name = 'django_tables2/bootstrap4.html'
#         fields = ('company_name', 'manager_name', 'address', 'email', 'phone_number', 'country', 'province')


# class SupplierTable(tables.Table):
#     edit = tables.TemplateColumn(template_name='inventory/suppliers/supplier_edit_column.html', verbose_name='Actions', orderable=False)

#     class Meta:
#         model = Supplier
#         template_name = 'django_tables2/bootstrap.html'
#         fields = ('company_name', 'manager_name', 'address', 'email', 'phone_number', 'country', 'province')

# inventory/tables.py
import django_tables2 as tables
from .models import Supplier, Producer
from django.urls import reverse
from django.utils.html import format_html

class SupplierTable(tables.Table):
    actions = tables.TemplateColumn(
        template_name='inventory/suppliers/supplier_actions.html',
        verbose_name='Actions',
        orderable=False
    )

    class Meta:
        model = Supplier
        template_name = 'django_tables2/bootstrap.html'
        fields = ('company_name', 'manager_name', 'address', 'phone_number', 'actions')


