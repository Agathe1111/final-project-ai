import json
import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = {"raw_document" : {"text" : text_to_analyse}}
    header = {"grpc-metadata-mm-model-id" : "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    status_code = response.status_code
    formatted_response = json.loads(response.text)
    emotion = formatted_response['emotionPredictions']['emotion']
    score = formatted_response['emotionPredictions']['score']
    #as the score is numbers, use the max() method
    dominant_emotion = max(formatted_response['emotionPredictions']['emotion']['score'])

    #error handling : if error 400, return None for all emotions. Else, return the emotion
    if status_code == 400 :
        return formatted_response = {
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness' : None,
            'dominant_emotion' : None
            }
    else :
        return formatted_response
        
