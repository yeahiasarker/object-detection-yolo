## Real Time Yolo Object Detection
This code is the implementation of [Yolov3](https://arxiv.org/abs/1804.02767) This object detection technique is being used widely in many industrial sectors. It can be said that yolov3 is a competitor of [SSD](https://arxiv.org/abs/1512.02325). Yolov3 can be used where speed is an important criteria. On the other hand, SSD can be used where accuracy is the main criteria. Earlier methods,([R-CNN](https://arxiv.org/abs/1311.2524), [Fast R-CNN](https://arxiv.org/abs/1504.08083)), a sliding window tried to locate objects in an image which is quite time consuming. [Faster R-CNN](https://arxiv.org/abs/1506.01497) uses Region Proposal Network (RPN) to identify bouding boxes. Yolov3 takes a completely different approach towards object detection. First it divides the image into grid of cells. Each cell is responsible for finding bounding boxes.
### Usage
- First download the pretrained weights and ncessary files from [here](https://pjreddie.com/media/files/yolov3.weights)
If you are using linux, just type in the terminal
~~~
wget https://pjreddie.com/media/files/yolov3.weights
~~~
- Install necessary modules. Type in the terminal
~~~
pip install opencv-python
~~~
~~~
pip install numpy
~~~

~~~
pip install imutils
~~~
<br>

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

Remember if you are using the builtin webcam of your laptop, you don't need to follow this process. After typing the command you will see only one port.
<br>
##### Here comes the main part
~~~ 
git clone https://github.com/goyeahia/object-detection-yolo
~~~
~~~ 
cd object-detection-yolo
~~~
 Now replace all the downloaded weight to the "yolo" folder and type this command in the terminal
~~~ 
python object_detection.py
~~~
###### Hurray !!! You did it !!!
If you are having any os compatiblity issue, let me know. I will try to fix as soon as possible. This mini project has been successfully run on ArchLinux.
