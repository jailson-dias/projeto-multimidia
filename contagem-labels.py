import json
import operator

file = open('output-api-imagga.json').read()
j = json.loads(file)
d = {}
for i in j:
	for x in i["results"][0]["tags"]:
		if x["tag"] in d:
			d[x["tag"]] += 1
		else:
			d[x["tag"]] = 1

a = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(list(a)[:41])