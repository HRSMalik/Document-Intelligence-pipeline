from pathlib import Path
from pypdf import PdfReader
from pypdf.errors import PdfReadError

def load_documents(path):
    documents = {}
    path = Path(path)

    if path.is_dir():
        files = list(path.iterdir())
    elif path.is_file():
        files = [path]
    else:
        raise ValueError("Invalid path")

    for file in files:
        text = ""
        if file.suffix.lower() == ".pdf":
            try:
                reader = PdfReader(file)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text
            except Exception as e:
                print(f"[WARN] Skipping invalid PDF: {file.name} ({e})")
                continue

        elif file.suffix.lower() == ".txt":
            try:
                text = file.read_text(errors="ignore")
            except Exception as e:
                print(f"[WARN] Skipping unreadable text file: {file.name}")
                continue
        else:
            continue

        cleaned_text = " ".join(text.split())

        if cleaned_text.strip():
            documents[file.name] = cleaned_text
        else:
            print(f"[WARN] No extractable text in: {file.name}")

    return documents
