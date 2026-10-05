## Live ASL Fingerspelling Classifier

Classifies American Sign Language alphabet hand signs from a webcam in real time. 
Compare two pipelines: a raw-pixel CNN and a hand-landmark MLP (MediaPipe). 
(Optional) Special case to handle J and Z, as they need motion capture.

# Recommended Datasets:
- Sign Language MNIST (J and Z excluded)
- ASL Alphabet (Kaggle) (J and Z excluded)
- Webcam test set (For testing only. 10-20 images per letter recorded by the team: varied people/lightning/background.)

# Evaluation 
- Accuracy
- A 24x24 confusion matrix
- (Optional) Speed and size: FPS and latency per frame
