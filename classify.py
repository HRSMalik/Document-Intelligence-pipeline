from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import numpy as np

DOCUMENT_CLASSES = ["Invoice", "Resume", "Utility Bill", "Other", "Unclassifiable"]

class SVMClassifier:
    def __init__(self):
        self.vectorizer = None
        self.classifier = None

    def train(self):
        training_samples = [
            ("Invoice number total amount due payment", "Invoice"),
            ("Curriculum vitae education experience skills", "Resume"),
            ("Electricity bill kWh usage amount due", "Utility Bill"),
            ("Internal meeting notes agenda discussion", "Other"),
            ("Unreadable random symbols data", "Unclassifiable")
        ]

        texts, labels = zip(*training_samples)

        self.vectorizer = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
        X = self.vectorizer.fit_transform(texts)

        self.classifier = SVC( kernel="linear", probability=True)
        self.classifier.fit(X, labels)

    def classify(self, text):
        vector = self.vectorizer.transform([text])
        label = self.classifier.predict(vector)[0]

        proba = self.classifier.predict_proba(vector)
        if len(proba.shape) == 1:
            confidence = float(np.max(proba))  
        else:
            confidence = float(np.max(proba))  

        return label, confidence