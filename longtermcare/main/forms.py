from django.forms import ModelForm
from .models import employee

class employeeFoam(ModelForm):
    class Meta:
        model = employee
        fields = ("name", "phone", "address", "preferTime") 