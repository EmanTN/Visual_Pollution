"""
 * Theme1 dataset image creating.
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2, os
import argparse


def plot_one_box(x, img, color=None, label=None, line_thickness=None, Inverted=False):
    # Plots one bounding box on image img
    tl = line_thickness or 2 # line thickness
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(img, c1, c2, color, thickness=tl)
    if label:
        tf = tl # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 2, thickness=tf)[0]
    if Inverted == True:
        c1 = c2
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    else:
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    
    cv2.rectangle(img, c1, c2, color, -1) # filled
    cv2.putText(img,label,(c1[0], c1[1] - 2),0,tl / 2,[225, 255, 255],thickness=tf,lineType=cv2.LINE_AA,)
    
    
#Parse arguments
parser = argparse.ArgumentParser()

# Add the three arguments with specific names
parser.add_argument("--image_path", default="./images", help="path to images.")
parser.add_argument("--result_file", default="labels.csv", help="name of result file of type .csv")
parser.add_argument("--output_path", default="predictions", help="path to save images with predictions")

args = parser.parse_args()

# Assign the parsed arguments to variables
image_path = args.image_path
result_file = args.result_file
output_path = args.output_path

# Using readlines()
result_file = open(result_file, 'r')
Lines = result_file.readlines()
count = 0
# Strips the newline character
for line in Lines:
    if count == 0:
        count += 1
        continue
    classNo = line.split(',')[0]
    file_id_path = line.split(',')[1]
    print(file_id_path)
    # open image in cv2
    img = cv2.imread(image_path + file_id_path)
    h, w, c = img.shape
    cat = line.split(',')[2]
    xmax = float(line.split(',')[3])
    xmin = float(line.split(',')[4])
    ymax = float(line.split(',')[5])
    ymin = float(line.split(',')[6]) 
    # plot the box
    plot_one_box([xmin, ymin, xmax, ymax], img, color=(0, 255, 0), label=cat, line_thickness=2)
    # save the image
    cv2.imwrite(output_path +  str(count) + "_" + str(int(float(classNo))) + "_" + file_id_path, img)
    print("Line {}: {}".format(count, line.strip()))
    count += 1
