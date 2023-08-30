from flask import Flask, request, send_from_directory, jsonify
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/upload', methods=['POST'])
def upload_video():
    video = request.files['video']
    video_filename = str(uuid.uuid4()) + video.filename
    video_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)
    video.save(video_path)

    # Process subtitle data and create subtitles file

    return jsonify({"message": "Video uploaded successfully"})

@app.route('/subtitles/<filename>')
def get_subtitles(filename):
    # Logic to retrieve subtitles file based on video filename
    subtitles_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename + '.srt')
    return send_from_directory(app.config['UPLOAD_FOLDER'], subtitles_file_path)

if __name__ == '__main__':
    app.run(debug=True)
