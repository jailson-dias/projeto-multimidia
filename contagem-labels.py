import json
import operator

# file = open('output-api-imagga-update.json').read()
# # file = open('output-api-imagga.json').read()
# j = json.loads(file)
# d = {}
# for i in j:
# 	for x in i["results"][0]["tags"]:
# 		if x["tag"] in d:
# 			d[x["tag"]] += 1
# 		else:
# 			d[x["tag"]] = 1

# a = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
# b = []

# for i in a[:20]:
# 	b.append(i[0])

# print(b)

def remover_fotos():
	lista = [
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image043.jpg",
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image050.jpg",
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image052.jpg",
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image131.jpg",
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image145.jpg",
	"https://raw.githubusercontent.com/msb55/projeto-multimidia/frontend/images/image146.jpg"
	]

	file = open('output-api-imagga-update.json').read()
	j = json.loads(file)
	out = []

	for i in j:
		if i["results"][0]["image"] in lista:
			print("Retirou " + i["results"][0]["image"])
		else:
			out.append(i)

	filew = open('output-api-imagga-update.json', 'w')
	filew.write(str(out).replace("'", "\"").replace("\"s ", "'s "))
	
remover_fotos()