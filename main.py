import io
import os
import csv
from os import listdir
from os.path import isfile, join
from time import sleep

# Imports the Google Cloud client library
from google.cloud import vision

path = os.path.join(os.path.dirname(__file__),'images')
images = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

# print (images)

columns = ['leg','shoulder','thigh','joint','muscle','structure','abdomen',
            'human leg','physical fitness','gym','girl','room','arm','weight training',
            'standing','photo shoot','trunk','sport venue','leggings','tights','shorts',
            'photography','beauty','model','undergarment']

csvfile =  open('data_input.csv', 'a')

writer = csv.writer(csvfile, delimiter=',')
linhas = 5
vision_client = vision.Client('plenary-network-146618')

while linha > 0:
    csvread =  open('data_input.csv', 'r')
    read = csv.reader(csvread, delimiter=',')

    linhas = len(list(csvread))

    csvread.close()

    if linhas<=0:
        writer.writerow(columns)

    # Instantiates a client
    try:
        for file_name in images[linhas-1:]:
            # Loads the image into memory
            image_file =  io.open(file_name, 'rb')
            content = image_file.read()
            image = vision_client.image(
                content=content)
            image_file.close()

        #     # print('properties:')
        #     # properties = image.detect_properties()


        #     # print('Labels:')
        #     # Performs label detection on the image file
            labels = image.detect_labels()

        #     # print (labels)
            row = []
            descs = [l.description for l in labels]
            print (descs)
            for column in columns:
                if column in descs:
                    idx = descs.index(column)
                    row.append(labels[idx].score)
                else:
                    row.append(0)
            writer.writerow(row)

    except Exception:
        linhas = 0
        print ("error")

csvfile.close()
csvlabel.close()