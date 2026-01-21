import streamlit as st
from ingest import load_documents
from extract import extract_invoice, extract_resume, extract_utility_bill
from classify import SVMClassifier
from retreiver import SemanticSearch

st.set_page_config(page_title="Document Intelligence Demo", layout="wide")
st.title("Document Intelligence Demo")
st.write("document extraction and semantic search.")

if "output" not in st.session_state:
    st.session_state.output = {}

if "search_engine" not in st.session_state:
    st.session_state.search_engine = SemanticSearch()

if "svm_classifier" not in st.session_state:
    st.session_state.svm_classifier = SVMClassifier()
    st.session_state.svm_classifier.train()

if st.button("Process Documents"):
    try:
        documents = load_documents("data")
        sorted_docs = dict(sorted(documents.items()))
        output = {}

        for filename, text in sorted_docs.items():
            label, confidence = st.session_state.svm_classifier.classify(text)

            if label not in ["Invoice", "Resume", "Utility Bill"]:
                continue

            record = {"class": label}

            if label == "Invoice":
                record.update(extract_invoice(text))
            elif label == "Resume":
                record.update(extract_resume(text))
            elif label == "Utility Bill":
                record.update(extract_utility_bill(text))

            output[filename] = record
            st.session_state.search_engine.add_documents([text])

        st.session_state.output = output
        st.success("Documents processed successfully!")
    except Exception as e:
        st.error(f"Error processing documents: {e}")

if st.session_state.output:
    st.subheader("Extracted Document Data")
    st.json(st.session_state.output)

st.divider()
st.subheader("Semantic Search")

query = st.text_input("Search documents by meaning")

if query:
    if not st.session_state.search_engine.texts:
        st.warning("No documents in the search index. Click 'Process Documents' first.")
    else:
        try:
            results = st.session_state.search_engine.search(query)
            if results:
                st.write("Search Results:")
                for idx, doc in enumerate(results, 1):
                    st.write(f"{idx}. {doc[:300]}{'...' if len(doc) > 300 else ''}")
            else:
                st.info("No results found.")
        except Exception as e:
            st.error(f"Error during search: {e}")
