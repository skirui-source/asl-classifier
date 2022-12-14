<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png" 
     width="200px"
     height="auto"/>
</p>

# <h1 align="center" id="heading">American-Sign-Language-classifier-CNN</h1>


## Files in this repository:

- demo - sample images
- MobileNet SavedModel - architecture, training configuration (optimizer, loss, metrics) and weights 
- model.py - load and pre-process input image for prediction 
- main.py -  FastAPI endpoint for display on webpage
- Dockerfile -  build dcontainerized app


## Requirements
python3 \
python-multipart \ 
tensorflow \
tensorflow-gpu \
keras \
fastapi==0.85.1 \
Pillow \
starlette==0.20.4 \
gunicorn \
uvicorn \
numpy


## signlanguage2text 
In this capstone project, I apply transfer-learning with two renowned pre-trained Convolutional Neural Network models
to classify asl hand gestures into text. The models were trained on open-source dataset (Kaggle), comprising 
2,500 samples across 36 classes (A-Z, 0-9). 


##  Neural Network
MOBILENET - accuracy 88% \
VGG16 - accuracy 20%


## PIPELINE 
INPUT (webcam/upload image) > PRE-PROCESSING > MACHINE LEARNING > DEPLOYMENT > OUTPUT 

![image](https://user-images.githubusercontent.com/71867292/196925283-e6808073-e4a5-43b6-8b9b-420f8c805903.png)


## References 
Dataset - https://www.kaggle.com/datasets/ayuraj/asl-dataset \
DockerHub repo - https://hub.docker.com/repository/docker/skirui11/mle8-final-capstone
