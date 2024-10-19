# forms.py
from django import forms
from .models import Device

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'type', 'hardware_id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'type': forms.TextInput(attrs={'class': 'block w-full rounded-md border-gray-300 shadow-sm'}),
            'hardware_id': forms.TextInput(attrs={
                'class': 'block w-full rounded-md border-gray-300 shadow-sm',
                'maxlength': '5',
                'pattern': '^[0-9]{5}$',
                'title': 'Hardware ID must be exactly 5 digits.',
            }),
        }

    def clean_hardware_id(self):
        hardware_id = self.cleaned_data.get('hardware_id')
        if not hardware_id.isdigit() or len(hardware_id) != 5:
            raise forms.ValidationError("Hardware ID must be exactly 5 digits.")
        return hardware_id