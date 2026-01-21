import json
from ingest import load_documents
from extract import extract_invoice, extract_resume, extract_utility_bill
from retreiver import SemanticSearch
from classify import SVMClassifier

documents = load_documents("data")
search_engine = SemanticSearch()

svm_classifier = SVMClassifier()
svm_classifier.train()

output = {}
sorted_docs = dict(sorted(documents.items()))

for filename, text in sorted_docs.items():
    label, confidence = svm_classifier.classify(text)
    if label not in ["Invoice", "Resume", "Utility Bill"]:
        continue

    record = {"class": label}

    if label == "Invoice":
        record.update(extract_invoice(text))
    elif label == "Resume":
        record.update(extract_resume(text))
    elif label == "Utility Bill":
        record.update(extract_utility_bill(text))
    
    else:
        continue

    output[filename] = record
    search_engine.add_documents([text])


with open("output.json", "w") as f:
    json.dump(output, f, indent=2)


print(search_engine.search("fine all resule with over 4 years of experience"))
