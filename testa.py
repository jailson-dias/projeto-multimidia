import io

from google.cloud import vision

def getdadosgoogle(file_name, follows):
    columns = ['leg','shoulder','thigh','joint','muscle','structure','abdomen',
            'human leg','physical fitness','gym','girl','room','arm','weight training',
            'standing','photo shoot','trunk','sport venue','leggings','tights','shorts',
            'photography','beauty','model','undergarment']
            
    vision_client = vision.Client('plenary-network-146618')
    
    # Instantiates a client
    try:
        image_file =  io.open(file_name, 'rb')
        content = image_file.read()
        image = vision_client.image(
            content=content)
        image_file.close()
        labels = image.detect_labels()

        row = []
        descs = [l.description for l in labels]
        print (descs)
        for column in columns:
            if column in descs:
                idx = descs.index(column)
                row.append(labels[idx].score)
            else:
                row.append(0)
        row.append(follows)
        return row

    except Exception:
        print ("error")
        return getdadosgoogle(file_name,follows)

# print (getdadosgoogle('images/image001.jpg',2541))