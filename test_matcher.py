from src.parser import extract_text_from_pdf
from src.nlp import extract_candidate_name

files = [
    'data/resumes/MOHAMMED FARIDH_Data_Engineer.pdf',
    'data/resumes/Bharath Servicenow HRSD.pdf',
]
for f in files:
    from src.parser import extract_text_from_pdf
    text = extract_text_from_pdf(f)
    print(f.split('/')[-1], '->', extract_candidate_name(text))
