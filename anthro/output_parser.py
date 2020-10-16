import sys
sys.path.append('/home/users/aditya/projects/anthro-data')
from api import DBAPI
from os.path import splitext, join, exists
import os
import json
import numpy as np

with open('input_ids.txt') as f:
    sample_ids = f.readlines()
sample_ids = [x.rstrip() for x in sample_ids]

if __name__ == '__main__':
    dbapi = DBAPI()
    ids, results = dbapi.select_by_key('state', 'telangana', ids=sample_ids)
    video_key = 'video_baby_ruler_chessboard'
    for result in results:
        image_folder = splitext(result[video_key])[0]
        coco_file, halpe_file = None, None
        if exists(join(image_folder, 'coco.json')):
            coco_file = join(image_folder, 'coco.json')
        if exists(join(image_folder, 'halpe_26.json')):
            halpe_file = join(image_folder, 'halpe_26.json')

        coco_kps, halpe_kps = [], []
        with open(coco_file) as f:
            coco = json.load(f)

        with open(halpe_file) as f:
            halpe = json.load(f)

        for line in coco:
            keypoint = np.array(line['keypoints']).reshape(-1, 3)
            coco_kps.append(keypoint)

        for line in halpe:
            keypoint = np.array(line['keypoints']).reshape(-1, 3)
            halpe_kps.append(keypoint)

        coco_kps = np.array(coco_kps)
        halpe_kps = np.array(halpe_kps)

        coco_npy = image_folder.rstrip('/') + '_coco_AP.npy'
        halpe_npy = image_folder.rstrip('/') + '_halpe_26_AP.npy'

        np.save(coco_npy, coco_kps)
        np.save(halpe_npy, halpe_kps)


