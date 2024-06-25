from django import forms
from ..models import Supplier, Producer
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        
    
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enregistrer'))
