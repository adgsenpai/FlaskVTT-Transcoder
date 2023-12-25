from flask import Flask, request, jsonify,render_template
import os

app = Flask(__name__)
 
def translate_file(file):
    file.save(file.filename) 
    return jsonify({'filename': file.filename + '.txt'})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.vtt'):
        return translate_file(file)

    return "Invalid file type", 400

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
if __name__ == '__main__':
    app.run(debug=True)