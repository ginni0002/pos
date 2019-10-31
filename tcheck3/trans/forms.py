from django import  forms
from .models import transactions
class transform(forms.ModelForm):
    class Meta:
        model=transactions
        fields=[
            'title',
            'transaction_id',
            'amount',
            'datetime',
            'TNcash',
            'TNcard'
        ]