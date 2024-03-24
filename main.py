
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gallery/')
def gallery():
    return render_template('gallery.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/images/')
def images():
    return send_from_directory('static/images', 'image.jpg')

@app.route('/image/<filename>')
def image(filename):
    return send_from_directory('static/images', filename)

if __name__ == '__main__':
    app.run(debug=True)
