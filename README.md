## American-Sign-Language-classifier using CNN


### Files in this repository:

- demo/: sample images uploaded via FastAPi webapp 
- mobilenet/: MobileNet SavedModel - architecture, training configuration (optimizer, loss, metrics) and weights 
- src/ : source code
    - model.py : 
    - main.py : 
- Dockerfile: build containerized app hosted in DockerHub repo (link) 


### Requirements
python3 \
pip3 \
tensorflow \
tensorflow-gpu \
keras \
fastapi==0.85.1 \
Pillow \
starlette==0.20.4 \
gunicorn \
uvicorn \
numpy \ 
python-multipart \ 


## signlanguage2text 
In this capstone project, I apply transfer-learning with two renowned pre-trained Convolutional Neural Network models (VGG16 and MobileNet)
to classify asl hand gestures into text. The model was trained on open-source dataset (Kaggle), comprising 
~2,500 samples with 36 classes (A-Z, 0-9). a

# Neural Network Models


TRAINING ACCURACY (MobileNet : 0.88) and (VGG16: 0.20)
