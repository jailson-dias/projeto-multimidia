from django.shortcuts import render

# Create your views here.

def home(request):
	if request.method == 'GET':
		return render(request, 'index.html')

	if request.method == 'POST':
		print("AKJSHF")
		print(request.__dict__)

def teste(request):
	print("AKJSHF")