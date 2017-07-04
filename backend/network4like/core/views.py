from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.forms import ImagemForm
from core.models import Imagem
from sklearn.externals import joblib

def home(request):
	if request.method == 'POST':
		# image = Imagem(file=request.FILES['uploaded_file'], qtd_likes=15) quantidade padrao para teste GUI
		image = Imagem(file=request.FILES['uploaded_file'])
		image.save()

		images = Imagem.objects.get(id=image.id)
		context = {
			'images': images
		}
        
        #carregar modelo
        #passar caminho para o .pkl
        # reg = joblib.load('caminho/para/modlel.pkl') 
        #pode chamar o metodo predict normalmente

		return render(request, 'results.html', context)

	else:
		return render(request, 'index.html')

def exibir(request, pk):
	image = Imagem.objects.get(id=pk)
	context = {
			'images': image
	}
	return render(request, 'results.html', context)