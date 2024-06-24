# inventory/tables.py
import django_tables2 as tables
from inventory.models import CompanyClient

class CompanyClientTable(tables.Table):
    actions = tables.TemplateColumn(template_name='inventory/clients_table_actions.html')

    class Meta:
        model = CompanyClient
        fields = ('nom', 'email', 'telephone')  # Champs à afficher dans le tableau
        template_name = 'django_tables2/bootstrap4.html'  # Template pour le style
