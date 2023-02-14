from django import forms
from CRUDFirst.models import EmpModel


class EmpForms(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """
    class Meta:
        model = EmpModel
        fields = '__all__'
