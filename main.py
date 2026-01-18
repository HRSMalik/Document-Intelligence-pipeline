import json
from ingest import load_documents
from extract import extract_invoice, extract_resume, extract_utility_bill
from retreiver import SemanticSearch
from intent import is_invoice, is_resume, is_utility_bill

documents = load_documents("data")
search_engine = SemanticSearch()

output = {}
sorted_docs = dict(sorted(documents.items()))

for filename, text in sorted_docs.items():

    if is_invoice(text):
        record = {"class": "Invoice"}
        record.update(extract_invoice(text))

    elif is_resume(text):
        record = {"class": "Resume"}
        record.update(extract_resume(text))

    elif is_utility_bill(text):
        record = {"class": "Utility Bill"}
        record.update(extract_utility_bill(text))

    else:
        continue

    output[filename] = record
    search_engine.add_documents([text])

with open("output.json", "w") as f:
    json.dump(output, f, indent=2)

print(search_engine.search("Find all documents mentioning payments due in January."))
