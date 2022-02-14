from django import forms

class EmployeeClientForm(forms.Form):
    id = forms.CharField(required=False, label="Id", initial='')
    name = forms.CharField(required=False, label="Name", initial='')