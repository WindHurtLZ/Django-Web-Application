# forms.py
import re

from django import forms
from .models import Device, Firmware


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].initial = 'CoAP'

class FirmwareUploadForm(forms.ModelForm):
    class Meta:
        model = Firmware
        fields = ['version', 'device_type', 'file']
        widgets = {
            'version': forms.TextInput(attrs={
                'class': 'form-input w-full max-w-md',
                'placeholder': 'v1.0.0',
                'id': 'version-input',
                'required': 'required',
            }),
            'device_type': forms.Select(attrs={
                'class': 'form-select w-full max-w-md',
                'id': 'device-type-select',
                'required': 'required',
            }),
            'file': forms.FileInput(attrs={
                'class': 'form-input w-full max-w-md',
                'id': 'file-input',
                'required': 'required',
            }),
        }

    def clean_version(self):
        version = self.cleaned_data.get('version')
        pattern = r'^v\d+\.\d+\.\d+$'
        if not re.match(pattern, version):
            raise forms.ValidationError('Version must be in the format vX.X.X where X is a number.')
        return version
