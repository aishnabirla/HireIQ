# from src.parser import extract_text_from_pdf
# from src.matcher import match_resume_to_jd

# jd_text = """
# We are looking for a Python developer with experience in
# machine learning, SQL, data analysis, and AI/ML.
# Knowledge of HTML, CSS and data visualization is preferred.
# Experience with SAP or ABAP is a plus.
# """

# resume_text = extract_text_from_pdf('data/resumes/Aishna Birla Resume one.pdf')
# result = match_resume_to_jd(jd_text, resume_text)

# print('Final Score:   ', result['final_score'], '%')
# print('TF-IDF Score:  ', result['tfidf_score'], '%')
# print('BERT Score:    ', result['bert_score'], '%')
# print('Skill Score:   ', result['skill_score'], '%')
# print('Matched Skills:', result['matched_skills'])
# print('Missing Skills:', result['missing_skills'])

from src.parser import extract_text_from_pdf, extract_text_from_string
from src.matcher import match_resume_to_jd
import os

jd_file_path = 'data/job_descriptions/jd1.txt'
with open(jd_file_path, 'r', encoding='utf-8') as f:
    jd_text = f.read()

print("JD loaded successfully!")
print("JD Preview:", jd_text[:200])
print("-" * 50)

resume_text = extract_text_from_pdf('data/resumes/Aishna Birla Resume one.pdf')
result = match_resume_to_jd(jd_text, resume_text)

print('Final Score:   ', result['final_score'], '%')
print('TF-IDF Score:  ', result['tfidf_score'], '%')
print('BERT Score:    ', result['bert_score'], '%')
print('Skill Score:   ', result['skill_score'], '%')
print('Matched Skills:', result['matched_skills'])
print('Missing Skills:', result['missing_skills'])

# from src.parser import extract_text_from_pdf
# from src.matcher import match_resume_to_jd

# jd_text = extract_text_from_pdf('data/job_descriptions/Senior_Data_Engineer_JD.pdf')
# resume_text = extract_text_from_pdf('data/resumes/LAKSHAY GOEL_Data_Engineer.pdf')

# result = match_resume_to_jd(jd_text, resume_text)

# print('Final Score:   ', result['final_score'], '%')
# print('TF-IDF Score:  ', result['tfidf_score'], '%')
# print('BERT Score:    ', result['bert_score'], '%')
# print('Skill Score:   ', result['skill_score'], '%')
# print('Matched Skills:', result['matched_skills'])
# print('Missing Skills:', result['missing_skills'])

# from src.parser import extract_text_from_pdf
# from src.nlp import extract_skills
# from src.matcher import calculate_skill_score, match_resume_to_jd, split_jd_sections

# jd_text = extract_text_from_pdf('data/job_descriptions/Senior_Data_Engineer_JD.pdf')
# resume_text = extract_text_from_pdf('data/resumes/LAKSHAY GOEL_Data_Engineer.pdf')

# print("=== JD Text Sample ===")
# print(repr(jd_text[:200]))
# print()

# required_text, preferred_text = split_jd_sections(jd_text)
# print("=== Required Section Preview ===")
# print(repr(required_text[:300]))
# print()
# print("=== Preferred Section Preview ===")
# print(repr(preferred_text[:300]))
# print()

# print("=== JD Skills (with jd_text) ===")
# jd_skills = extract_skills(jd_text, jd_text)
# print(jd_skills)
# print(f"Total: {len(jd_skills)}")
# print()

# print("=== Required Section Skills ===")
# req_skills = extract_skills(required_text, required_text)
# print(req_skills)
# print(f"Total: {len(req_skills)}")
# print()

# print("=== Resume Skills ===")
# resume_skills = extract_skills(resume_text, jd_text)
# print(resume_skills)
# print(f"Total: {len(resume_skills)}")
# print()

# score, matched, missing = calculate_skill_score(jd_text, resume_text)
# print(f"Skill Score: {round(score * 100, 2)}%")
# print(f"Matched: {matched}")
# print(f"Missing: {missing}")