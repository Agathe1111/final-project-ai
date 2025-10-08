#Step one : import flask (for deployment), render_template (for render html index page), 
#requests (for using get and post requests)
#Import module emotiondetector
from flask import Flask, render_template, requests
from EmotionDetector.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

#Step two : define the routes : need of the route to the emotiondetector, and the route to the index html page
#Route to EmotionDetector
@app.route('/emotionDetector')
def sent_emotion_detector():
    #1 : get the parameters of the user input
    text_to_analyse = request.args.get('textToAnalyze')
    #2 : send back to the user the results once analysed
    response = emotion_detector(text_to_analyse)
    response_formatted_text = f"For the input you gave, the results are : \
     'anger' : {response['anger']}, 'sadness' : {response['sadness']}, \
     'joy' : {response['joy']}, 'disgust' : {response['disgust']}, \
     'fear' : {response['fear']}. For you given input, the dominant emotion is :\
      {response['dominant_emotion']}"
    #if invalid input
    if dominant_emotion is None:
        return "Invalid input ! Try again !"
    else:
        #return the response_formatted_text variable
        return response_formatted_text

#Route to the html index page
@app.route('/')
def render_index_page():
    return render_template('index.html')

#Run the app in a localhost
if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 5000)


