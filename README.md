# Biomechanics-of-gait
Topic : Biomechanics of gait with image processing for classification of normal and abnormal gait.</br>
Knowledge : Image processing, Computer vision, Machine learning, Disease or symptom about abnormal gait.</br>
Tools : Python, OpenCV, Mediapipe, Numpy.</br></br>

## About project


<img src = "Limping gait.gif" />

## Installation
To use the Biomechanics of gait, follow these step :</br></br>
<a href = "https://www.python.org/downloads/">Install python</a> <a>from version 3.9 onwards.</a>
</br></br>
install libraries :
```
  python -m pip install opencv-python mediapipe numpy
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

change code in BiomechanicOfGait.py line 11 to your videos you need to check [File name].[File type] :
```
  cap = cv2.VideoCapture("[File name].[File type]")
```

run :
```
  python BiomechanicsOfGait.py
```

output :</br>
============================== Conclude ==============================</br>
 Gait abnormal - risk : [none / neck pain / limping / hip hike / no arm swing]</br>
======================================================================</br>



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
