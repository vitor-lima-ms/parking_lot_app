from django import forms

"""Form to create instances of the Driver model"""
class DriverRegisterForm(forms.Form):
    driver_name = forms.CharField(max_length=50)
    monthly = forms.BooleanField(required=False)
    cnh = forms.CharField(max_length=11)
    cpf = forms.CharField(max_length=11)
    file_upload = forms.FileField(required=False)

"""Form to search for drivers by name"""
class DriverSearchForm(forms.Form):
    name_search = forms.CharField(max_length=50)