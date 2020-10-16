import sys
sys.path.append('/home/users/aditya/projects/anthro-data')
from api import DBAPI
from os.path import splitext, join, exists
import os

with open('input_ids.txt') as f:
    sample_ids = f.readlines()
sample_ids = [x.rstrip() for x in sample_ids]

if __name__ == '__main__':
    dbapi = DBAPI()
    ids, results = dbapi.select_by_key('state', 'telangana', ids=sample_ids)
    video_key = 'video_baby_ruler_chessboard'
    for result in results:
        image_folder = splitext(result[video_key])[0]
        cmd = f'bash coco.sh {image_folder}'
        os.system(cmd)

        cmd = f'bash halpe.sh {image_folder}'
        os.system(cmd)



