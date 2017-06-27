import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
vision_client = vision.Client('plenary-network-146618')

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'images/image007.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(
        content=content)

print('properties:')
properties = image.detect_properties()


print('Labels:')
# Performs label detection on the image file
labels = image.detect_labels()

columns = ['muscle', 'arm', 'leg', 'abdomen', 'fitness', 'thigh']
x = []
for label in labels:
    print(label.description)
    if label.description in columns:
    	x.append(label.score)
    print(label.score)
print(x)