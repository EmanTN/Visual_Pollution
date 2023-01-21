# Visual_Pollution
## Smartathon Hackathon

1. Image Size: 1920x 1080

2. Multiply bounding boxes points by 2 to get exact coordinates.

3. Submit predicted boxes as if image size is:  960 x 1080

4. Number of classes is 11
   
5. Number of images in the train dataset is 7874 

6. Number of images in the test dataset is 2092

7. Evaluation score = 100 * mean average precision (mAP)

8. Total number of objects is 19,950 in 7874 images

<pre>
No. objects	  Category 
1555	      BAD_BILLBOARD 
1		      BAD_STREETLIGHT 
83		      BROKEN_SIGNAGE 
2253	      CLUTTER_SIDEWALK
2730	      CONSTRUCTION_ROAD
107		      FADED_SIGNAGE
8597	      GARBAGE 
1124		  GRAFFITI 
2625	      POTHOLES 
748		      SAND_ON_ROAD 
127		      UNKEPT_FACADE
</pre>

---
### Software
YOLO v3: https://github.com/ultralytics/yolov3 </br>
Python 3: https://www.python.org/
---
### Training YOLO v3
xx
---
### Making Predictions
xx
---
### Postprocessing data to create .csv file of results
xx
---
### Create images with predictions
xx

