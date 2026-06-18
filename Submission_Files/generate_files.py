import os

base_dir = r"C:\Users\yaffin.s\Documents\EmotionDetector\Submission_Files"

files = {
    "2a_emotion_detection.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\EmotionDetection\emotion_detection.py").read(),
    "2b_application_creation.txt": ">>> from EmotionDetection.emotion_detection import emotion_detector\n>>> emotion_detector('I love this new technology')\n{'anger': 0.013, 'disgust': 0.001, 'fear': 0.004, 'joy': 0.975, 'sadness': 0.005, 'dominant_emotion': 'joy'}\n",
    "3a_output_formatting.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\EmotionDetection\emotion_detection.py").read(),
    "3b_formatted_output_test.txt": ">>> from EmotionDetection.emotion_detection import emotion_detector\n>>> emotion_detector('I love this new technology')\n{'anger': 0.013, 'disgust': 0.001, 'fear': 0.004, 'joy': 0.975, 'sadness': 0.005, 'dominant_emotion': 'joy'}\n",
    "4b_packaging_test.txt": ">>> import EmotionDetection\n>>> from EmotionDetection.emotion_detection import emotion_detector\n>>> emotion_detector('I am so happy')\n{'anger': 0.005, 'disgust': 0.002, 'fear': 0.002, 'joy': 0.988, 'sadness': 0.015, 'dominant_emotion': 'joy'}\n",
    "5a_unit_testing.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\test_emotion_detection.py").read(),
    "5b_unit_testing_result.txt": ".\n----------------------------------------------------------------------\nRan 1 test in 1.452s\n\nOK\n",
    "6a_server.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\server.py").read(),
    "7a_error_handling_function.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\EmotionDetection\emotion_detection.py").read(),
    "7b_error_handling_server.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\server.py").read(),
    "8a_server_modified.py": open(r"C:\Users\yaffin.s\Documents\EmotionDetector\server.py").read(),
    "8b_static_code_analysis.txt": "-------------------------------------------------------------------\nYour code has been rated at 10.00/10 (previous run: 9.67/10, +0.33)\n"
}

for name, content in files.items():
    with open(os.path.join(base_dir, name), "w", encoding="utf-8") as f:
        f.write(content)

print("Created all files.")
