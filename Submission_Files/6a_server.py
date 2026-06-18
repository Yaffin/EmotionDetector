"""
Server module for the Emotion Detector web application.
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Renders the main application page over the Flask channel
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the emotion of the provided text and returns a formatted string.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
