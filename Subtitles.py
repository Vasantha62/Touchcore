import speech_recognition as sr

def generate_subtitles_from_audio(audio_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Subtitles not generated"

# Inside the video upload endpoint
subtitle_text = generate_subtitles_from_audio(video_path)

# Save the generated text as subtitles
subtitles_filename = video_filename + '.srt'  # You can modify this as needed
subtitles_path = os.path.join(app.config['UPLOAD_FOLDER'], subtitles_filename)

with open(subtitles_path, 'w') as subtitles_file:
    subtitles_file.write(subtitle_text)

# Now, you have generated subtitles and saved them to a file
