import json

with open('./data/annotations.json') as f:
    data = json.load(f)
    for i in range(4608):
        with open('./data/annotations/' + str(data['images'][str(i+1)])[:-4] + '.json', 'w') as new_f:
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
