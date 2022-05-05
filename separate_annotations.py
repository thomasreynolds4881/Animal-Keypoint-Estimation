import json
from os.path import isfile

with open('./data/annotations.json') as f:
    data = json.load(f)
    for i, a in enumerate(data['annotations']):
        name = './data/annotations/' + str(data['images'][str(a['image_id'])])[:-4] + '.json'
        
        # check if file already made
        if isfile(name):
            # append to the json
            with open(name, 'r') as existing_f:
                exist_data = json.loads(existing_f.read())
                exist_data['bboxes'].append(a['bbox'])
                exist_data['keypoints'].append(a['keypoints'])
            with open(name, 'w') as existing_f:
                existing_f.write(str(exist_data).replace('\'', '\"'))

        else:
            # create new json file
            with open(name, 'w') as new_f:
                j_data = data['annotations'][i]
                del j_data['image_id']
                del j_data['num_keypoints']
                del j_data['category_id']
                temp = [j_data['keypoints']]
                del j_data['keypoints']
                j_data['bboxes'] = [j_data['bbox']]
                del j_data['bbox']
                j_data['keypoints'] = temp
                new_f.write(str(j_data).replace('\'', '\"'))
