# Biomechanics-of-gait
Topic : Biomechanics of gait with image processing for classification of normal and abnormal gait.</br>
Knowledge : Image processing, Computer vision, Machine learning, Disease or symptom about abnormal gait.</br>
Tools : Python, OpenCV, Mediapipe, Numpy.</br></br>

## About project
This project aims to investigate the possibility of abnormal gait in order to identify any anomalies in the body and also intends to study image processing.</br>
(-) Using Mediapipe for detect landmarks of human bodies in an image or video.</br>
(-) Using OpenCV to read data from image or video.</br>
(-) Using Numpy for calculate math equations to determine risk of gait.</br></br>

<img src = "Other/(GIF)Limping gait.gif" />
</br>

## Installation
To use the Biomechanics of gait, follow these step :</br></br>
<a href = "https://www.python.org/downloads/">Install python</a> <a>from version 3.9 onwards.</a>
</br></br>
install libraries :
```
  python3 -m pip install opencv-python mediapipe numpy
```

install my project :</br>
```
  git clone https://github.com/watcharapol28/Biomechanics-of-gait.git
```
</br>

## Running
To run the Biomechanics of gait, follow these step :</br></br>
upload files gait videos that want to check in the folder Biomechanics-of-gait or in same the folder as BiomechanicsOfGait.py.
</br></br>

open folder :
```
  cd Biomechanics-of-gait
```
2 choice with your videos you need to check</br>
( - ) change your video file name you need to check to gait.mp4 in folder Dataset</br>
( - ) change code in BiomechanicOfGait.py line 11 to your videos you need to check [File name].[File type] :

```
  cap = cv2.VideoCapture("./Dataset/[File name].[File type]")
```

run :
```
  python3 BiomechanicsOfGait.py
```

output :</br>
Conclude gait abnormal - risk : [none / neck pain / limping / hip hike / no arm swing]</br>
</br></br>


<h2>Scope</h2>
<h3>First thought</h3>
- Check some disease with abnormal gait</br>
- Check some symptoms from abnormal gait</br>
- Check risk for some symptoms from abnormal gait</br>
<h3>Done</h3>
- Risk for neck pain.</br>
- Risk for limping gait.</br>
- Risk for Hip hike.</br>
- No arm swing.</br>
<h3>Problem</h3>
- Must be viewed from the side only.</br>
- Did not use AI for training or prediction.</br>
- Quite a bit of relevant information or research.</br>
- Datasets related to various diseases are quite rare.</br>
<h3>Continue in the future</h3>
- Use AI for train model or predict disease.</br>
- Applied with accessories for greater accuracy.</br>
