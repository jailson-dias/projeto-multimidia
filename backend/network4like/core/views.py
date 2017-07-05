from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.core.urlresolvers import reverse_lazy

from core.forms import ImagemForm
from core.models import Imagem

import requests
import json

import imp
import codecs

def home(request):
	if request.method == 'POST':
		image = Imagem(file=request.FILES['uploaded_file_1'], qtd_followers=request.POST['qtd_followers'])
		image.save()
		
		prefix = 'C:\\Users\\barre\\Documents\\projeto-multimidia\\projeto-multimidia\\backend\\network4like\\media\\'
		i = open(prefix + image.file.name, 'rb')

		api_key = 'acc_05cd943bb73fdbb'
		api_secret = 'bf19cef5ee73254c26e47746004a8155'
		
		print(image.file.url)
		response = requests.post('https://api.imagga.com/v1/content',
			auth=(api_key, api_secret),
			files={'image': i})
		result = response.json()

		content_id = result['uploaded'][0]['id']

		response = requests.get('https://api.imagga.com/v1/tagging?content=%s' % content_id,
                        auth=(api_key, api_secret))

		result = response.json()
		print(str(result))
		columns = ['person', 'adult', 'people', 'caucasian', 'attractive', 
		'happy', 'lifestyle', 'pretty', 'smile', 'model', 'portrait', 'lady', 
		'women', 'body', 'fashion', 'human', 'smiling', 'one', 'sexy', 'cute']

		tags = result["results"][0]["tags"]
		row = []
		for column in columns:
			if len([row.append(x["confidence"]) for x in tags if x['tag'] == column]) <= 0:
				row.append(0)

		# print(row)

		row.append(int(request.POST['qtd_followers']))
		print(row)
		script = imp.load_source('resultado', 'C:\\Users\\barre\\Documents\\projeto-multimidia\\projeto-multimidia\\resultado.py')
		likes = script.treinamento(row)
		print('NUMPY???')
		print(str(likes))
		print(str(result))	
		
		image.qtd_likes = int(likes)
		image.save()
		context = {
			'images': image
		}

		return render(request, 'results.html', context)

	else:
		return render(request, 'index.html')

def exibir(request, pk):
	image = Imagem.objects.get(id=pk)
	context = {
			'images': image
	}
	return render(request, 'results.html', context)

	