from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

DOCUMENT_CLASSES = [
    "Invoice",
    "Resume",
    "Utility Bill",
    "Other",
    "Unclassifiable"
]

def train_classifier():
    training_samples = [
        ("Invoice number total amount due payment", "Invoice"),
        ("Curriculum vitae education experience skills", "Resume"),
        ("Electricity bill kWh usage amount due", "Utility Bill"),
        ("Internal meeting notes agenda discussion", "Other"),
        ("Unreadable random symbols data", "Unclassifiable")
    ]

    texts, labels = zip(*training_samples)

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    X = vectorizer.fit_transform(texts)

    classifier = LinearSVC()
    classifier.fit(X, labels)

    return vectorizer, classifier


def classify_document(text, vectorizer, classifier):
    vector = vectorizer.transform([text])
    return classifier.predict(vector)[0]
