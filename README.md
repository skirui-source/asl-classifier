## American-Sign-Language-classifier using CNN
### Fourthbrain Mle8 final capstone project


### Files in this repository:

- demo/: images to demonstrate the model's accuracy- uploaded via FastAPi webapp 
- mobilenet/: MobileNet SavedModel
    model's architecture, training configuration (optimizer, loss, metrics) and weights 
- src/ : source code
    - model.py : 
    - main.py : 
- Dockerfile: instructions to build containerized app hosted in DockerHub repo 


### Requirements
python3
pip3
tensorflow
tensorflow-gpu
keras
fastapi==0.85.1
Pillow
starlette==0.20.4
gunicorn
uvicorn
numpy
python-multipart


## sign2text 
In this capstone project, I apply transfer-learning with two renowned pre-trained Convolutional Neural Network models (VGG16 and MobileNet)
to translate american sign language hand gestures into text. The model was trained on open-source dataset (Kaggle), comprising 
~2,500 samples with 36 classes (A-Z, 0-9). a

# 
