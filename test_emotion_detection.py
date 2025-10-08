#1 : import unittest and the module to put under test
import unittest
from emotion_detection import emotion_detector
#2 : create a test class
    class TestEmotionDetector(unittest.TestCase):
        def test_emotion_detector(self):
            result1 = emotion_detector('I am glad this happened')
            self.assertEqual(result1["dominant_emotion"], "joy")
            result2 = emotion_detector('I am really angry about that !')
            self.assertEqual(result2["dominant_emotion"], "anger")
            result3 = emotion_detector('I feel disgust just by hearing about it !')
            self.assertEqual(result3["dominant_emotion"], "disgust")
            result4 = emotion_detector('I am so sad about it')
            self.assertEqual(result4["dominant_emotion"], "sadness")
            result5 = emotion_detector('I fear so much this happen')
            self.assertEqual(result5["dominant_emotion"], "fear")
#3 : call the test
unittest.main()