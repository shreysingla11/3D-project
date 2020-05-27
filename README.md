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

Details for implementation:

Project 1:
It was basically to get an idea of transfer learning and hyperparameter tuning using PyTorch library. It can be implemented
by downloading the 5-Gestures dataset and running the notebook (Change the path to dataset in the notebook and set
it to where you have downloaded the dataset). You can also add more images in the set as per your convenience.
Warning: Do not try this without gpu. You can use google colab though as it provides free gpu.

Project 2:
It was to use the model for live video streams. If you want to train the model, download the Gestures-5 dataset and run
the notebook Hand_Gestures-mymodel.ipynb (change the path to dataset) the trained model will be saved in your working
directory. You can also use the pretrained weigths which are present in my_model-hangestures.pt. Download the weights in
the working directory and run the notebook Handgestures-vid.ipynb. The gesture name is shown on the screen with a bar graph
showing the probability distribution of each gesture.

Project 3:
It was to implement the idea of one-shot learning to predict hand gestures. To experiment with the 15-gestures model, 
Download the 15-gestures dataset and run the notebook (change the data-path in the notebook). Trained model is saved
in the working directory. To train the model for 25-way prediction, download the 25 Gestures dataset and run the notebook
Siamese_handgestures_25_2.ipynb (change the data-path). The trained model is saved in your working directory.
To use the pretrained model, download the model from siamese-model.txt and run the notebook Siamese_handgestures_pretrained-final.ipynb.
Note: The directory structure should be-
      oneshot-test -> train (one image per gesture with name gesture.jpg)
                   -> test (one test image)
      Also it would be better if you add some more images in the 25-gestures dataset to introduce more variance and
      retrain the model (only if you have a gpu instance).
      Warning: The number of images in each gesture should be same and change shape of X in Siamese_handgestures_25_2.ipynb
               accordingly.
               
Project 4:
It was to get an idea of Flask and REST api. Download the cats_vs_dogs_acc.h5 and make the directory structure as follows-
Flask -> api2.py
      -> cats_vs_dogs_acc.h5
      -> templates -> index3.html
Open the terminal in required directory and run $python api2.py
