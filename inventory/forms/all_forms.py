from django import forms
from ..models import Supplier, Producer, CompanyClient, PersonalClient, Product, Province, Sale, Purchase
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
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})   

class CompanyClientForm(forms.ModelForm):
    class Meta:
        model = CompanyClient
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})

class PersonalClientForm(forms.ModelForm):
    class Meta:
        model = PersonalClient
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})

class ProvinceFormForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})  

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
            if isinstance(field.widget, forms.widgets.CheckboxInput):
                field.widget.attrs.update({'class': 'form-check-input'})
            if isinstance(field.widget, forms.widgets.FileInput):
                field.widget.attrs.update({'class': 'form-control-file'})
                
# class SupplierForm(forms.ModelForm):
#     class Meta:
#         model = Supplier
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'post'
#         self.helper.add_input(Submit('submit', 'Enregistrer'))
