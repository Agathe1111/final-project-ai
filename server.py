#Step one : import flask (for deployment), render_template (for render html index page), 
#requests (for using get and post requests)
#Import module emotiondetector
from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask('Emotion Detection')

#Step two : define the routes : need of the route to the emotiondetector, and the route to the index html page
#Route to EmotionDetector
@app.route('/emotionDetector')
def sent_emotion_detector():
    #1 : get the parameters of the user input
    text_to_analyse = request.args.get('textToAnalyze')

    #1-1 : if no input :
    if not text_to_analyse:
    return "Invalid input ! Please write something."

    #2 : send back to the user the results once analysed
    response = emotion_detector(text_to_analyse)
    
    #if invalid input
    if response['dominant_emotion'] is None:
        return "Invalid input ! Try again !"
    #if valid input
    else:
        #return the response_formatted_text variable
        response_formatted_text = (f"For the input you gave, the results are : "
        f"'anger' : {response['anger']}, 'sadness' : {response['sadness']}, "
        f"'joy' : {response['joy']}, 'disgust' : {response['disgust']}, "
        f"'fear' : {response['fear']}. For you given input, the dominant emotion is : {response['dominant_emotion']}")
        return response_formatted_text

#Route to the html index page
@app.route('/')
def render_index_page():
    return render_template('index.html')

#Run the app in a localhost
if __name__ == '__main__' :
    app.run(host = '0.0.0.0', port = 5000)


