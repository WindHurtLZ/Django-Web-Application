# forms.py
from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'type': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
        }
