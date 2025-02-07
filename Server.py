
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='/')

# Enable CORS for all domains (you can specify origins if needed)
CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5173"}})

# Define a temporary upload folder for audio files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    audio_file = request.files['file']
    if audio_file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the file temporarily
    audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_file.filename)
    audio_file.save(audio_path)

    return jsonify({'message': 'File successfully uploaded', 'file_path': audio_path}), 200


if __name__ == '__main__':
    app.run(debug=True)
