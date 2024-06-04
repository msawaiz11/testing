from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
import base64
from flask_socketio import SocketIO
from io import BytesIO
import base64
from PIL import Image
from PIL import Image
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('crop')
def handle_crop(data):
    startx = data['startX']
    starty = data['startY']
    width = data['width']
    height = data['height']
    imgsrc = data['imageSrc']
    image_data = base64.b64decode(imgsrc.split(',')[1])  # Remove data:image/jpeg;base64,
    image = Image.open(BytesIO(image_data))
    cropped_image = image.crop((startx, starty, startx + width, starty + height))
    cropped_image = cropped_image.convert('RGB')

    cropped_image.save("cropped_image22.jpg")


    # print("Crop data received:", imgsrc)


@socketio.on('connect')
def on_connect():
    print("Client connected")


@socketio.on('disconnect')
def on_disconnect():
    print("Client disconnected")



if __name__ == "__main__":
    socketio.run(app)
    # app.run(debug=True, port=5330)
