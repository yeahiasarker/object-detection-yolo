## Real Time Yolo Object Detection
This code is the implementation of [Yolov3](https://arxiv.org/abs/1804.02767) This object detection technique is being used widely in many industrial sectors. It can be said that yolov3 is a competitor of [SSD](https://arxiv.org/abs/1512.02325). Yolov3 can be used where speed is an important criteria. On the other hand, SSD can be used where accuracy is the main criteria. Earlier methods,([R-CNN](https://arxiv.org/abs/1311.2524), [Fast R-CNN](https://arxiv.org/abs/1504.08083)), a sliding window tried to locate objects in an image which is quite time consuming. [Faster R-CNN](https://arxiv.org/abs/1506.01497) uses Region Proposal Network (RPN) to identify bouding boxes. Yolov3 takes a completely different approach towards object detection. First it divides the image into grid of cells. Each cell is responsible for finding bounding boxes.
### Usage
- First download the pretrained weights and ncessary files from here.
Now for webcam the default webcam port is 0. If you are using any external webcam, just change the port number with your ip address of ip camera or the external port.
#### How To Check Webcam Port Number In Linux
First type this command in the terminal
~~~ 
ls /dev/video*
~~~
* Now eject the external webcam. Again type the same command.
~~~
ls /dev/video*
~~~
* You can see the a port is missing. That's the desired port of our external webcam.
<br>

Remember if you are using the builtin webcam of your laptop, you don't need to follow this process. After pressing the command you will see only one port.
<br>
##### Here comes the main part
~~~ 
git clone 
~~~
~~~ 
cd ...
~~~
 Now replace all the downloaded files to the "yolo" folder
~~~ 
python object_detection.py
~~~
###### Hurray !!! You did it !!!
