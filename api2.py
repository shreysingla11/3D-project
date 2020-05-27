
from keras.applications import VGG16
import flask
from flask import Flask, request, render_template
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import keras

from keras.applications import VGG16

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template('index3.html')


@app.route("/predict", methods=['POST'])
def make_prediction():
    if request.method == 'POST':
        file = request.files['image']
        if not file:
            return render_template('index3.html', label='No File')
        img_path = file
        img = image.load_img(img_path, target_size=(150,150))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = x/255
        features = conv_base.predict(x)
        features = np.reshape(features, (1, 4*4*512))
        p = model.predict(features)
        if p<0.5:
            label='cat'
            pred = str((1-p)*100)
        else:
            label='dog'
            pred = str(p*100)
        return render_template('index3.html', label=label,percent=pred)

if __name__ == '__main__':
    conv_base = VGG16(weights='imagenet', include_top=False,
                      input_shape=(150, 150, 3))
    model = load_model('cats_vs_dogs_acc.h5')
    app.run(host='0.0.0.0', port=8000, debug=False, threaded=False)
