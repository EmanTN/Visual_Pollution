import pandas as pd
import numpy as np
import matplotlib.image as img
import os
import sys

path = '/Users/tundeaderinwale/Hackaton/dataset/'
train_data = pd.read_csv(path + 'train.csv')
train_data['class'].unique(),train_data['name'].unique(),train_data['name'].unique().shape
def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


for image in train_data.image_path:

     data = train_data.query('image_path == "' + image + '"')
     # copy image to train path
     os.system('cp ' + path + 'images/' + image + ' ' + path + 'images/train/')

     # convert bounding box for each segment
     label_str = ''
     for box in data.index:
          d = data.loc[box, :]
          b = (float(d.xmin), float(d.xmax), float(d.ymin), float(d.ymax))
          bb = convert((1080, 1920), b)
          b_str = str(int(d['class'])) + " " + " ".join([str(a) for a in bb]) + '\n'
          label_str += b_str

          # create label file
     with open(path + 'labels/train/' + image.replace('jpg', 'txt'), 'w') as fh:
          fh.write(label_str)
     # break

test_data = pd.read_csv(path + 'test.csv')
for image in test_data.image_path:
     # copy image to test path
     os.system('cp ' + path + 'images/' + image + ' ' + path + 'images/test/')
