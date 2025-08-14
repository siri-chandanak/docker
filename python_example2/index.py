from PIL import Image
from flask import Flask, send_file
# Load the image
img = Image.open("sample.jpg")

# Print basic info
print(f"Image format: {img.format}")
print(f"Image size: {img.size[0]} x {img.size[1]} pixels")
print(f"Image mode: {img.mode}")


app = Flask(__name__)

@app.route('/')
def show_image():
    return send_file("sample.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
