# 3D-project

My Work

Project 1:
First I experimented with th 5 gestures dataset. I trained the upper layers of famous object detection models such as 
VGG-16, ResNet, GoogleNet, Densenet etc. trained on ImageNet dataset using transfer learning. The respective codes are
present in the repo with link to colab.

Project 2:
Next I trained a CNN model from scratch on 5 gestures dataset. The model is there in the repo (my_model-hangestures.pt).
The code used for learning is Hand_Gestures-mymodel.ipynb. I used the model for predicting gestures from live video (the
code for same is Handgestures-vid.ipynb) and used it to control many mouse and keyboard events using PyAutoGui library.
I specifically embedded the gestures in dino game in chrome.

Project 3:
I also experimented with Siamesem Neural Network idea for predicting gestures using one-shot learning. The original
Siamese Network is SiameseNet.ipynb. First I trained my siamese net on 15 gestures dataset. The code for same is 
siamese_hand_gestures-1.ipynb and siamese_hand_gestures-2.ipynb. Then I modified the model slightly (basically
made the model light so that it does not take much space) and after some hyperparameter tuning, I trained the model
on 25 gestures dataset. The final code for training is Siamese_handgestures_25_2.ipynb. The link to model is 
siamese-model.txt. I got a whopping 98% 25-way validation accuracy. The code for using pretrained weights for 
one-shot learning is Siamese_handgestures_pretrained-final.ipynb.

Project 4:
I also made a simple cat-vs-dog classifier that classifies the images as cat or dog and deployed it on web 
server using Flask and REST Api. The pretrained model is cats_vs_dogs_acc.h5. The main app is api.py and the 
template is index3.html. 

