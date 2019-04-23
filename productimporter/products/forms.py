from django import forms
from .models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model=Products
        fields='__all__'


from .models import Document
from .tasks import load_to_db_task
class DocumentForm(forms.ModelForm):
    def save_to_db(self):
        load_to_db_task.delay()
    class Meta:
        model = Document
        fields = ('description', 'document', )