from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

BASE_MUSIC_PATH = os.path.join(os.getcwd(), "music")
MOODS = ["happy", "sad", "angry", "neutral"]

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  

@app.route('/songs/<mood>')
def get_songs(mood):
    if mood not in MOODS:
        return jsonify({"error": "Invalid mood"}), 400

    folder_path = os.path.join(BASE_MUSIC_PATH, mood)
    if not os.path.exists(folder_path):
        return jsonify([])

    # List all MP3 files in the folder
    songs = [f for f in os.listdir(folder_path) if f.lower().endswith(".mp3")]
    return jsonify(songs)

@app.route('/songs/<mood>/<filename>')
def serve_song(mood, filename):
    if mood not in MOODS:
        return "Invalid mood", 400
    folder_path = os.path.join(BASE_MUSIC_PATH, mood)
    return send_from_directory(folder_path, filename)

if __name__ == "__main__":
    app.run(debug=True)
