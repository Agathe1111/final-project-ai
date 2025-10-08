#1 : import unittest and the module to put under test
import unittest
from EmotionDetector.emotion_detection import emotion_detector
#2 : create a test class
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1["dominant_emotion"], "joy")

        result_2 = emotion_detector('I am really angry about that !')
        self.assertEqual(result_2["dominant_emotion"], "anger")

        result_3 = emotion_detector('I feel disgust just by hearing about it !')
        self.assertEqual(result_3["dominant_emotion"], "disgust")

        result_4 = emotion_detector('I am so sad about it')
        self.assertEqual(result_4["dominant_emotion"], "sadness")

        result_5 = emotion_detector('I fear so much this happen')
        self.assertEqual(result_5["dominant_emotion"], "fear")

#3 : call the test
if __name__ == "__main__":
    unittest.main()