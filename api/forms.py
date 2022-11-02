from django.forms import ModelForm
from .models import Balance




class BalanceForm(ModelForm):
      class Meta:
            models = Balance
            fields =('name', 'code', 'status')