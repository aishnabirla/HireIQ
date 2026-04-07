print("Testing all library imports...")
print("-" * 40)

try:
    import pdfplumber
    print("pdfplumber     : OK -", pdfplumber.__version__)
except:
    print("pdfplumber     : FAILED - run pip install pdfplumber")

try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("spaCy          : OK -", spacy.__version__)
except:
    print("spaCy          : FAILED - run python -m spacy download en_core_web_sm")

try:
    import nltk
    print("NLTK           : OK -", nltk.__version__)
except:
    print("NLTK           : FAILED - run pip install nltk")

try:
    import sklearn
    print("scikit-learn   : OK -", sklearn.__version__)
except:
    print("scikit-learn   : FAILED - run pip install scikit-learn")

try:
    import streamlit
    print("Streamlit      : OK -", streamlit.__version__)
except:
    print("Streamlit      : FAILED - run pip install streamlit")

try:
    import bcrypt
    print("bcrypt         : OK")
except:
    print("bcrypt         : FAILED - run pip install bcrypt")

try:
    import pandas
    print("pandas         : OK -", pandas.__version__)
except:
    print("pandas         : FAILED - run pip install pandas")

try:
    import fpdf
    print("fpdf2          : OK")
except:
    print("fpdf2          : FAILED - run pip install fpdf2")

try:
    import openpyxl
    print("openpyxl       : OK -", openpyxl.__version__)
except:
    print("openpyxl       : FAILED - run pip install openpyxl")

try:
    from sentence_transformers import SentenceTransformer
    print("sentence-transformers : OK")
except:
    print("sentence-transformers : FAILED - run pip install sentence-transformers")

print("-" * 40)
print("Test complete!")