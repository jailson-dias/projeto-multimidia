import requests
import json

api_key = 'acc_05cd943bb73fdbb'
api_secret = 'bf19cef5ee73254c26e47746004a8155'
image_url_base = 'https://raw.githubusercontent.com/fbormann/projeto-intromultimidia/master/images/image001.jpg'

fw = open("output.json", 'a')

# for i in range(10,18):
# for i in range(1,54):
response = requests.get('https://api.imagga.com/v1/tagging?url=https://raw.githubusercontent.com/msb55/projeto-multimidia/master/images/image012.png', 
	auth=(api_key, api_secret))
	
j = response.json()
fw.write(str(j).replace("'", "\"") + "\n")


# Requisição passagem a imagem como arquivo, e não o link

# response = requests.post('https://api.imagga.com/v1/content',
	# auth=(api_key, api_secret),
	# files={'image': open(image_path, 'r')})
# print response.json()