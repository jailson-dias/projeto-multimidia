from django import forms
from core.models import Imagem

class ImagemForm(forms.ModelForm):

	class Meta:
		model = Imagem
		fields=['file']