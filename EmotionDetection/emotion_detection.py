"""
Emotion detection module using Watson NLP library.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion of the provided text.
    """
    if not text_to_analyze:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = ('https://sn-watson-emotion.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=10)

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotion_predictions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)

        return {
            'anger': emotion_predictions['anger'],
            'disgust': emotion_predictions['disgust'],
            'fear': emotion_predictions['fear'],
            'joy': emotion_predictions['joy'],
            'sadness': emotion_predictions['sadness'],
            'dominant_emotion': dominant_emotion
        }

    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return None
