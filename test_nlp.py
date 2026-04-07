"""
test_nlp.py
Run from project root: python test_nlp.py
Tests name, email, education, experience extraction
for all resumes in data/resumes/
"""

import os
from src.parser import extract_text_from_pdf
from src.nlp import (
    extract_candidate_name,
    extract_candidate_email,
    extract_education,
    extract_experience,
    extract_skills,
    process_resume
)

# ── Config ──
RESUMES_FOLDER = "data/resumes"
JD_PATH        = "data/job_descriptions/Senior_Data_Engineer_JD.pdf"

# ── Load JD text ──
jd_text = ""
if os.path.exists(JD_PATH):
    jd_text = extract_text_from_pdf(JD_PATH)
    print(f" JD loaded: {len(jd_text)} chars\n")
else:
    print(f"  JD not found at {JD_PATH} — skill extraction will use DB only\n")

print("=" * 70)

# ── Process each resume ──
resume_files = sorted([
    f for f in os.listdir(RESUMES_FOLDER)
    if f.endswith('.pdf')
])

if not resume_files:
    print(f" No PDF files found in {RESUMES_FOLDER}")
    exit()

for filename in resume_files:
    path = os.path.join(RESUMES_FOLDER, filename)
    print(f"\n FILE: {filename}")
    print("-" * 50)

    # Extract raw text
    text = extract_text_from_pdf(path)

    if not text or len(text.strip()) < 50:
        print("  Could not extract text from this PDF")
        continue

    print(f"  Raw text length : {len(text)} chars")
    print(f"  First 200 chars : {repr(text[:200])}")
    print()

    # Test each extractor individually
    name      = extract_candidate_name(text)
    email     = extract_candidate_email(text)
    education = extract_education(text)
    experience = extract_experience(text)
    skills    = extract_skills(text, jd_text)

    print(f"  Name       : {name}")
    print(f"  Email      : {email}")
    print(f"  Education  : {education[:120]}{'...' if len(education) > 120 else ''}")
    print(f"  Experience : {experience[:120]}{'...' if len(experience) > 120 else ''}")
    print(f"  Skills     : {sorted(skills)}")
    print(f"  Skill count: {len(skills)}")
    print("=" * 70)

print("\n Done.")