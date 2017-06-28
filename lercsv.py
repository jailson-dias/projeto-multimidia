import json
import csv
import operator

def ler():
    csvread =  open('trainning.csv', 'r')
    read = csv.reader(csvread, delimiter=',')

    tags = {}

    for row in read:
        for tag in row:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1

    tags = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)
    print(tags[:30])
    csvread.close()

def escrever():
    columns = ['adult','caucasian','person','people','attractive','lifestyle',
    'happy','smile','pretty','model','human','fashion','portrait','lady', 'body',
    'women', 'smiling', 'black', 'happiness', 'sexy', 'one', 'face', 'hair', 
    'posing', 'cute', 'healthy', 'clothing'
    , 'youth', 'health', 'looking', 'fitness', 'studio', 'fit', 'brunette'
    , 'fun', 'slim', 'pose', 'holding', 'cheerful', 'sensual', 'glamour']
    
    # csvread =  open('output-api-imagga.json', 'r')
    # read = csv.reader(csvread, delimiter=',')
    file = open('output-api-imagga.json').read()
    j = json.loads(file)

    csvfile =  open('data_input.csv', 'a')
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(columns)
    for linha in j:
        # print (linha)
        descs = linha["results"][0]["tags"]
        # print (descs)
        row = []
        for column in columns:
            if len([row.append(x["confidence"]) for x in descs if x['tag'] == column]) <= 0:
                row.append(0)

        # print (row)
        writer.writerow(row)
    csvfile.close()

ler()
