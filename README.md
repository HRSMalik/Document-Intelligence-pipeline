# Document Intelligence Pipeline

This project implements a local AI system for document understanding, classification, data extraction, and retrieval using open-source tools only. It processes PDF and text documents, classifies them into categories (Invoice, Resume, Utility Bill, Other, Unclassifiable), extracts structured data, and provides semantic search capabilities.

## Python Environment Setup

It's recommended to use a virtual environment to isolate the project's dependencies from your system Python installation. This prevents conflicts with other projects and ensures reproducible results.

### Using venv (built-in Python module)

1. Create a virtual environment:
   ```
   python -m venv doc_intel_env
   ```

2. Activate the virtual environment:
   - On Windows: `doc_intel_env\Scripts\activate`
   - On macOS/Linux: `source doc_intel_env/bin/activate`

3. Deactivate when done: `deactivate`

### Using conda (if you have Anaconda/Miniconda installed)

1. Create a conda environment:
   ```
   conda create -n doc_intel_env python=3.8
   ```

2. Activate the environment:
   ```
   conda activate doc_intel_env
   ```

3. Deactivate when done: `conda deactivate`

## Installation

1. Ensure you have Python 3.8 or higher installed on your system.

2. Clone or download this repository to your local machine.

3. Navigate to the project directory:
   ```
   cd /path/to/Document-Intelligence-pipeline
   ```

4. (Optional but recommended) Activate your virtual environment as described above.

5. Install the required dependencies using pip:
   ```
   pip install -r requirement.txt
   ```

   This will install all necessary libraries including pypdf, scikit-learn, sentence-transformers, faiss-cpu, numpy, pandas, and tqdm.

## Usage

1. Place your PDF or text documents in the `data/` folder. The system supports PDF files (using pypdf for text extraction) and plain text files.

2. Run the main processing script:
   ```
   python main.py
   ```

3. The program will:
   - Load and process all documents from the `data/` folder
   - Classify each document based on content signals
   - Extract structured data for classified documents
   - Build a semantic search index
   - Output results to `output.json`

4. View the results in `output.json`, which contains classifications and extracted fields for each processed document.

## Libraries and Methods Used

This project uses the following open-source libraries and methods, chosen for their reliability, performance, and suitability for local, offline AI processing:

- **pypdf**: 
  - **Purpose**: Reads and extracts text content from PDF files, handling multi-page documents with robust error handling for corrupted or problematic PDFs.
  - **Why chosen**: It's a pure Python library that doesn't require external dependencies like Poppler, making it easy to install and use across different platforms. Alternatives like PyPDF2 were considered but pypdf offers better performance and active maintenance.

- **scikit-learn**: 
  - **Purpose**: Provides machine learning algorithms for document classification.
  - **Specific components used**:
    - `TfidfVectorizer`: Converts raw text into numerical TF-IDF (Term Frequency-Inverse Document Frequency) features, which capture the importance of words in the context of the entire document collection.
    - `LinearSVC`: A linear Support Vector Machine classifier that efficiently categorizes documents based on their TF-IDF features.
  - **Why chosen**: Scikit-learn is the go-to library for classical machine learning in Python. It's well-documented, optimized, and integrates seamlessly with numpy. For this use case, TF-IDF + SVM provides a lightweight yet effective classification approach that doesn't require large amounts of training data.

- **sentence-transformers**: 
  - **Purpose**: Generates high-quality sentence embeddings for semantic search using the "all-MiniLM-L6-v2" model, which produces 384-dimensional vectors.
  - **Why chosen**: This library provides pre-trained transformer models specifically fine-tuned for sentence similarity tasks. The "all-MiniLM-L6-v2" model strikes a good balance between performance and computational efficiency, running quickly on CPU while providing state-of-the-art semantic understanding. It's preferred over raw Hugging Face transformers for its ease of use and optimized sentence encoding.

- **faiss-cpu**: 
  - **Purpose**: Implements efficient similarity search and clustering of dense vectors using L2 (Euclidean) distance for the retrieval system.
  - **Why chosen**: FAISS (Facebook AI Similarity Search) is one of the fastest libraries for nearest neighbor search, capable of handling millions of vectors efficiently. The CPU version is used here for simplicity and to avoid GPU dependencies. It's crucial for the semantic search functionality, allowing quick retrieval of relevant documents based on meaning rather than exact keyword matches.

- **numpy**: 
  - **Purpose**: Handles numerical operations, particularly for managing embeddings and vector operations in the semantic search pipeline.
  - **Why chosen**: As the fundamental package for scientific computing in Python, numpy provides efficient array operations that are essential for working with high-dimensional embeddings. It's a dependency of most ML libraries and provides the backbone for numerical computations in this project.

- **pandas**: 
  - **Purpose**: Included for potential data manipulation and analysis tasks (though not heavily used in the current implementation).
  - **Why chosen**: Pandas is the standard library for data manipulation in Python. While the current pipeline uses simple JSON output, pandas could be useful for more complex data processing or analysis in future extensions.

- **tqdm**: 
  - **Purpose**: Provides progress bars for long-running operations (if implemented in future enhancements).
  - **Why chosen**: Tqdm is a lightweight, widely-used library for adding progress indicators to loops and operations, improving user experience during potentially time-consuming document processing.

### Pipeline Components

1. **Ingestion (`ingest.py`)**: Loads documents from a specified folder, extracts text from PDFs using pypdf, and cleans the text by normalizing whitespace.

2. **Intent Classification (`intent.py`)**: Uses a simple but effective keyword-based approach to classify documents. It looks for specific signal words (e.g., "invoice", "total amount" for invoices) and requires a minimum number of matches to classify, avoiding false positives.

3. **Data Extraction (`extract.py`)**: Applies regular expression patterns to extract structured fields from classified documents. Each document type has custom regex patterns designed to capture relevant information like dates, amounts, and contact details.

4. **Retrieval (`retreiver.py`)**: Implements semantic search by encoding documents into embeddings using SentenceTransformers, then using FAISS for efficient similarity search. This allows users to find documents by meaning rather than exact keywords.
