# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
# from src.nlp import extract_skills
# import numpy as np

# model = SentenceTransformer('all-MiniLM-L6-v2')


# def calculate_tfidf_score(jd_text, resume_text):
#     try:
#         vectorizer = TfidfVectorizer(
#             stop_words='english',
#             ngram_range=(1, 1),   # FIX: bigrams on 2-doc corpus add noise, unigrams are cleaner
#             min_df=1
#         )
#         vectors = vectorizer.fit_transform([jd_text, resume_text])
#         score = cosine_similarity(vectors[0], vectors[1])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"TF-IDF error: {e}")
#         return 0.0


# def calculate_bert_score(jd_text, resume_text):
#     try:
#         # FIX: removed [:512] character truncation — sentence-transformers
#         # tokenizer handles max token length internally. Truncating by character
#         # was cutting off most of the resume content and killing semantic scores.
#         embeddings = model.encode([jd_text, resume_text], show_progress_bar=False)
#         score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"BERT error: {e}")
#         return 0.0


# EQUIVALENT_SKILLS = [
#     {"spark", "pyspark", "apache spark"},
#     {"kafka", "apache kafka"},
#     {"airflow", "apache airflow"},
#     {"hadoop", "apache hadoop"},
#     {"postgres", "postgresql"},
#     {"gcp", "google cloud"},
#     {"aws", "amazon web services"},
#     {"azure", "microsoft azure"},
#     {"scikit-learn", "sklearn"},
#     {"kubernetes", "k8s"},
#     {"git", "github"},
#     {"js", "javascript"},
#     {"ts", "typescript"},
# ]


# def skills_match(skill1, skill2):
#     skill1 = skill1.lower().strip()
#     skill2 = skill2.lower().strip()
#     if skill1 == skill2:
#         return True
#     if skill1 in skill2 or skill2 in skill1:
#         return True
#     for group in EQUIVALENT_SKILLS:
#         if skill1 in group and skill2 in group:
#             return True
#     return False


# def find_matched_skills(jd_skills, resume_skills):
#     matched = []
#     missing = []
#     for jd_skill in jd_skills:
#         found = False
#         for resume_skill in resume_skills:
#             if skills_match(jd_skill, resume_skill):
#                 found = True
#                 break
#         if found:
#             matched.append(jd_skill)
#         else:
#             missing.append(jd_skill)
#     return matched, missing


# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_lower = jd_text.lower()
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         required_section = ""
#         preferred_section = ""

#         if "required" in jd_lower:
#             parts = jd_lower.split("required")
#             if len(parts) > 1:
#                 required_section = parts[1][:800]

#         if "preferred" in jd_lower or "nice to have" in jd_lower:
#             split_word = "preferred" if "preferred" in jd_lower else "nice to have"
#             parts = jd_lower.split(split_word)
#             if len(parts) > 1:
#                 preferred_section = parts[1][:500]

#         required_skills = list(extract_skills(required_section)) if required_section else list(extract_skills(jd_text))
#         preferred_skills = list(extract_skills(preferred_section)) if preferred_section else []

#         matched_required, missing_required = find_matched_skills(required_skills, resume_skills)
#         matched_preferred, missing_preferred = find_matched_skills(preferred_skills, resume_skills)

#         all_matched = list(set(matched_required + matched_preferred))
#         all_missing = list(set(missing_required))

#         total_required = len(required_skills) if required_skills else 1
#         total_preferred = len(preferred_skills) if preferred_skills else 0

#         required_score = len(matched_required) / total_required if total_required > 0 else 0
#         preferred_score = len(matched_preferred) / total_preferred if total_preferred > 0 else 0

#         final_skill_score = (required_score * 0.8) + (preferred_score * 0.2)

#         return round(float(final_skill_score), 4), all_matched, all_missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []

# def calculate_final_score(tfidf_score, bert_score, skill_score):
#     final = (tfidf_score * 0.2) + (bert_score * 0.4) + (skill_score * 0.4)
#     return round(final * 100, 2)


# def match_resume_to_jd(jd_text, resume_text):
#     tfidf_score = calculate_tfidf_score(jd_text, resume_text)
#     bert_score = calculate_bert_score(jd_text, resume_text)
#     skill_score, matched_skills, missing_skills = calculate_skill_score(
#         jd_text, resume_text
#     )
#     final_score = calculate_final_score(tfidf_score, bert_score, skill_score)
#     return {
#         "final_score": final_score,
#         "tfidf_score": round(tfidf_score * 100, 2),
#         "bert_score": round(bert_score * 100, 2),
#         "skill_score": round(skill_score * 100, 2),
#         "matched_skills": matched_skills,
#         "missing_skills": missing_skills
#     }


# def rank_resumes(jd_text, resumes):
#     results = []
#     for resume in resumes:
#         match = match_resume_to_jd(jd_text, resume["text"])
#         results.append({
#             "name": resume["name"],
#             "email": resume["email"],
#             "file_name": resume["file_name"],
#             "final_score": match["final_score"],
#             "tfidf_score": match["tfidf_score"],
#             "bert_score": match["bert_score"],
#             "skill_score": match["skill_score"],
#             "matched_skills": match["matched_skills"],
#             "missing_skills": match["missing_skills"]
#         })
#     results.sort(key=lambda x: x["final_score"], reverse=True)
#     return results







# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
# from src.nlp import extract_skills
# import numpy as np

# model = SentenceTransformer('all-MiniLM-L6-v2')


# def calculate_tfidf_score(jd_text, resume_text):
#     try:
#         vectorizer = TfidfVectorizer(
#             stop_words='english',
#             ngram_range=(1, 1),
#             min_df=1
#         )
#         vectors = vectorizer.fit_transform([jd_text, resume_text])
#         score = cosine_similarity(vectors[0], vectors[1])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"TF-IDF error: {e}")
#         return 0.0


# def calculate_bert_score(jd_text, resume_text):
#     try:
#         # No [:512] truncation — sentence-transformers tokenizer handles it internally
#         embeddings = model.encode([jd_text, resume_text], show_progress_bar=False)
#         score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"BERT error: {e}")
#         return 0.0


# EQUIVALENT_SKILLS = [
#     {"spark", "pyspark", "apache spark"},
#     {"kafka", "apache kafka"},
#     {"airflow", "apache airflow"},
#     {"hadoop", "apache hadoop"},
#     {"postgres", "postgresql"},
#     {"git", "github"},
#     {"etl", "elt"},
#     {"kubernetes", "k8s"},
#     {"ci/cd", "jenkins"},
#     {"databricks", "delta lake"},
# ]


# def skills_match(skill1, skill2):
#     skill1 = skill1.lower().strip()
#     skill2 = skill2.lower().strip()
#     if skill1 == skill2:
#         return True
#     if skill1 in skill2 or skill2 in skill1:
#         return True
#     for group in EQUIVALENT_SKILLS:
#         if skill1 in group and skill2 in group:
#             return True
#     return False


# def find_matched_skills(jd_skills, resume_skills):
#     matched = []
#     missing = []
#     for jd_skill in jd_skills:
#         found = any(skills_match(jd_skill, rs) for rs in resume_skills)
#         if found:
#             matched.append(jd_skill)
#         else:
#             missing.append(jd_skill)
#     return matched, missing







# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_lower = jd_text.lower()
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         required_section = ""
#         preferred_section = ""

#         if "required" in jd_lower:
#             parts = jd_lower.split("required")
#             if len(parts) > 1:
#                 required_section = parts[1][:2000]

#         if "preferred" in jd_lower or "nice to have" in jd_lower:
#             split_word = "preferred" if "preferred" in jd_lower else "nice to have"
#             parts = jd_lower.split(split_word)
#             if len(parts) > 1:
#                 preferred_section = parts[1][:1000]

#         required_skills = list(extract_skills(required_section)) if required_section else list(extract_skills(jd_text))
#         preferred_skills = list(extract_skills(preferred_section)) if preferred_section else []

#         matched_required, missing_required = find_matched_skills(required_skills, resume_skills)
#         matched_preferred, _ = find_matched_skills(preferred_skills, resume_skills)

#         all_matched = list(set(matched_required + matched_preferred))
#         all_missing = list(set(missing_required))

#         total_required  = len(required_skills)  if required_skills  else 1
#         total_preferred = len(preferred_skills) if preferred_skills else 0

#         required_score  = len(matched_required)  / total_required  if total_required  > 0 else 0
#         preferred_score = len(matched_preferred) / total_preferred if total_preferred > 0 else 0

#         final_skill_score = (required_score * 0.8) + (preferred_score * 0.2)

#         return round(float(final_skill_score), 4), all_matched, all_missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []

# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_skills = set(extract_skills(jd_text))
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         if not jd_skills:
#             return 0.0, [], []

#         matched = []
#         missing = []
#         for jd_skill in jd_skills:
#             # Use skills_match for alias-aware comparison
#             found = any(skills_match(jd_skill, rs) for rs in resume_skills)
#             if found:
#                 matched.append(jd_skill)
#             else:
#                 missing.append(jd_skill)

#         score = len(matched) / len(jd_skills)
#         return round(float(score), 4), matched, missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []

# OLD — simple approach
    # jd_skills = set(extract_skills(jd_text))
    # resume_skills = set(extract_skills(resume_text, jd_text))
    # matched = jd_skills.intersection(resume_skills)
    # score = len(matched) / len(jd_skills)

# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_skills = set(extract_skills(jd_text))
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         matched = []
#         missing = []

#         for jd_skill in jd_skills:
#             found = False
#             for resume_skill in resume_skills:
#                 if skills_match(jd_skill, resume_skill):
#                     found = True
#                     break
#             if found:
#                 matched.append(jd_skill)
#             else:
#                 missing.append(jd_skill)

#         score = len(matched) / len(jd_skills) if jd_skills else 0
#         return round(float(score), 4), matched, missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []







# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_skills = list(extract_skills(jd_text))
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         if not jd_skills:
#             return 0.0, [], []

#         matched, missing = find_matched_skills(jd_skills, resume_skills)
#         score = len(matched) / len(jd_skills)

#         return round(float(score), 4), matched, missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []

# def calculate_final_score(tfidf_score, bert_score, skill_score):
#     # BERT 50% — semantic understanding, most reliable signal
#     # TF-IDF 30% — keyword overlap
#     # Skill 20% — explicit skill match boost
#     final = (tfidf_score * 0.1) + (bert_score * 0.7) + (skill_score * 0.2)
#     return round(final * 100, 2)


# def match_resume_to_jd(jd_text, resume_text):
#     tfidf_score = calculate_tfidf_score(jd_text, resume_text)
#     bert_score  = calculate_bert_score(jd_text, resume_text)
#     skill_score, matched_skills, missing_skills = calculate_skill_score(jd_text, resume_text)
#     final_score = calculate_final_score(tfidf_score, bert_score, skill_score)
#     return {
#         "final_score":    final_score,
#         "tfidf_score":    round(tfidf_score * 100, 2),
#         "bert_score":     round(bert_score  * 100, 2),
#         "skill_score":    round(skill_score * 100, 2),
#         "matched_skills": matched_skills,
#         "missing_skills": missing_skills
#     }


# def rank_resumes(jd_text, resumes):
#     results = []
#     for resume in resumes:
#         match = match_resume_to_jd(jd_text, resume["text"])
#         results.append({
#             "name":           resume["name"],
#             "email":          resume["email"],
#             "file_name":      resume["file_name"],
#             "final_score":    match["final_score"],
#             "tfidf_score":    match["tfidf_score"],
#             "bert_score":     match["bert_score"],
#             "skill_score":    match["skill_score"],
#             "matched_skills": match["matched_skills"],
#             "missing_skills": match["missing_skills"]
#         })
#     results.sort(key=lambda x: x["final_score"], reverse=True)
#     return results






# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
# from src.nlp import extract_skills
# import numpy as np
# import re

# model = SentenceTransformer('all-MiniLM-L6-v2')


# def calculate_tfidf_score(jd_text, resume_text):
#     try:
#         vectorizer = TfidfVectorizer(
#             stop_words='english',
#             ngram_range=(1, 1),
#             min_df=1
#         )
#         vectors = vectorizer.fit_transform([jd_text, resume_text])
#         score = cosine_similarity(vectors[0], vectors[1])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"TF-IDF error: {e}")
#         return 0.0


# def calculate_bert_score(jd_text, resume_text):
#     try:
#         embeddings = model.encode([jd_text, resume_text], show_progress_bar=False)
#         score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
#         return round(float(score), 4)
#     except Exception as e:
#         print(f"BERT error: {e}")
#         return 0.0


# EQUIVALENT_SKILLS = [
#     {"spark", "pyspark", "apache spark"},
#     {"kafka", "apache kafka"},
#     {"airflow", "apache airflow"},
#     {"hadoop", "apache hadoop"},
#     {"postgres", "postgresql"},
#     {"git", "github"},
#     {"etl", "elt", "etl/elt"},
#     {"kubernetes", "k8s"},
#     {"ci/cd", "jenkins", "cicd"},
#     {"databricks", "delta lake"},
#     {"ml", "machine learning", "ai/ml", "artificial intelligence"},
#     {"data pipeline", "data pipelines", "data engineering", "etl"},
#     {"redshift", "aws redshift"},
#     {"bigquery", "google bigquery"},
# ]

# PREMIUM_INSTITUTES = [
#     "iit", "nit", "iim", "bits pilani", "vit", "manipal",
#     "mit", "stanford", "harvard", "oxford", "cambridge",
#     "national institute of technology", "indian institute of technology",
#     "indian institute of management"
# ]

# CERTIFICATION_KEYWORDS = [
#     "aws certified", "azure certified", "gcp certified",
#     "google professional", "databricks certified",
#     "snowflake certified", "pmp", "prince2",
#     "scrum master", "cissp", "comptia",
#     "tensorflow developer", "pytorch certified",
#     "az-900", "az-104", "dp-900", "dp-203",
#     "solutions architect", "cloud practitioner",
#     "professional data engineer", "machine learning specialty"
# ]


# def skills_match(skill1, skill2):
#     skill1 = skill1.lower().strip()
#     skill2 = skill2.lower().strip()
#     if skill1 == skill2:
#         return True
#     if len(skill1) > 3 and len(skill2) > 3:
#         if skill1 in skill2 or skill2 in skill1:
#             return True
#     for group in EQUIVALENT_SKILLS:
#         if skill1 in group and skill2 in group:
#             return True
#     return False


# def find_matched_skills(jd_skills, resume_skills):
#     matched = []
#     missing = []
#     for jd_skill in jd_skills:
#         found = any(skills_match(jd_skill, rs) for rs in resume_skills)
#         if found:
#             matched.append(jd_skill)
#         else:
#             missing.append(jd_skill)
#     return matched, missing


# def calculate_skill_score(jd_text, resume_text):
#     try:
#         jd_skills = list(extract_skills(jd_text))
#         resume_skills = set(extract_skills(resume_text, jd_text))

#         if not jd_skills:
#             return 0.0, [], []

#         matched, missing = find_matched_skills(jd_skills, resume_skills)
#         score = len(matched) / len(jd_skills)

#         return round(float(score), 4), matched, missing

#     except Exception as e:
#         print(f"Skill match error: {e}")
#         return 0.0, [], []


# def calculate_experience_score(jd_text, resume_text):
#     try:
#         jd_lower = jd_text.lower()
#         resume_lower = resume_text.lower()

#         jd_range = re.findall(
#             r'(\d+)\s*[-to]+\s*(\d+)\s*years?', jd_lower
#         )
#         jd_min_only = re.findall(
#             r'(\d+)\+\s*years?', jd_lower
#         )

#         resume_years = re.findall(
#             r'(\d+)\+?\s*years?\s*(?:of\s*)?(?:experience|exp)?',
#             resume_lower
#         )

#         if not resume_years:
#             return 0.5

#         candidate_years = max([int(y) for y in resume_years if int(y) < 50])

#         if jd_range:
#             jd_min = int(jd_range[0][0])
#             jd_max = int(jd_range[0][1])
#         elif jd_min_only:
#             jd_min = int(jd_min_only[0])
#             jd_max = jd_min + 5
#         else:
#             return 0.6

#         if jd_min <= candidate_years <= jd_max:
#             return 1.0
#         elif candidate_years > jd_max:
#             return 0.9
#         elif candidate_years >= jd_min - 2:
#             return 0.7
#         else:
#             return 0.4

#     except Exception as e:
#         print(f"Experience score error: {e}")
#         return 0.5


# def calculate_title_score(jd_text, resume_text):
#     try:
#         jd_lower = jd_text.lower()
#         resume_lower = resume_text.lower()

#         title_patterns = [
#             "data engineer", "software engineer", "data scientist",
#             "ml engineer", "machine learning engineer",
#             "data analyst", "devops engineer", "backend developer",
#             "full stack developer", "frontend developer",
#             "product manager", "project manager", "business analyst",
#             "solutions architect", "cloud engineer", "ai engineer",
#             "nlp engineer", "research scientist", "data architect"
#         ]

#         jd_title = None
#         resume_title = None

#         for pattern in title_patterns:
#             if pattern in jd_lower:
#                 jd_title = pattern
#                 break

#         for pattern in title_patterns:
#             if pattern in resume_lower:
#                 resume_title = pattern
#                 break

#         if not jd_title or not resume_title:
#             return 0.5

#         if jd_title == resume_title:
#             return 1.0
#         elif jd_title in resume_title or resume_title in jd_title:
#             return 0.85
#         else:
#             jd_words = set(jd_title.split())
#             resume_words = set(resume_title.split())
#             overlap = jd_words.intersection(resume_words)
#             if overlap:
#                 return 0.6
#             return 0.3

#     except Exception as e:
#         print(f"Title score error: {e}")
#         return 0.5


# def calculate_certification_score(jd_text, resume_text):
#     try:
#         resume_lower = resume_text.lower()
#         jd_lower = jd_text.lower()

#         resume_certs = []
#         for cert in CERTIFICATION_KEYWORDS:
#             if cert in resume_lower:
#                 resume_certs.append(cert)

#         if not resume_certs:
#             return 0.4

#         jd_mentions_certs = any(
#             word in jd_lower for word in
#             ["certified", "certification", "certificate"]
#         )

#         if jd_mentions_certs and resume_certs:
#             return min(0.7 + len(resume_certs) * 0.1, 1.0)
#         elif resume_certs:
#             return 0.7

#         return 0.5

#     except Exception as e:
#         print(f"Certification score error: {e}")
#         return 0.5


# def calculate_education_score(resume_text):
#     try:
#         resume_lower = resume_text.lower()

#         for institute in PREMIUM_INSTITUTES:
#             if institute in resume_lower:
#                 return 1.0

#         if any(kw in resume_lower for kw in ["ph.d", "phd", "doctorate"]):
#             return 1.0
#         if any(kw in resume_lower for kw in ["m.tech", "m.s.", "master", "mba", "m.sc"]):
#             return 0.85
#         if any(kw in resume_lower for kw in ["b.tech", "b.e.", "bachelor", "b.sc", "bca"]):
#             return 0.75
#         if "diploma" in resume_lower:
#             return 0.6

#         return 0.5

#     except Exception as e:
#         print(f"Education score error: {e}")
#         return 0.5


# def calculate_final_score(tfidf_score, bert_score, skill_score,
#                            experience_score=0.5, title_score=0.5,
#                            cert_score=0.5, edu_score=0.5):
#     final = (
#         tfidf_score      * 0.10 +
#         bert_score       * 0.30 +
#         skill_score      * 0.30 +
#         experience_score * 0.12 +
#         title_score      * 0.10 +
#         cert_score       * 0.05 +
#         edu_score        * 0.03
#     )
#     return round(final * 100, 2)


# def match_resume_to_jd(jd_text, resume_text):
#     tfidf_score = calculate_tfidf_score(jd_text, resume_text)
#     bert_score = calculate_bert_score(jd_text, resume_text)
#     skill_score, matched_skills, missing_skills = calculate_skill_score(
#         jd_text, resume_text
#     )
#     experience_score = calculate_experience_score(jd_text, resume_text)
#     title_score = calculate_title_score(jd_text, resume_text)
#     cert_score = calculate_certification_score(jd_text, resume_text)
#     edu_score = calculate_education_score(resume_text)

#     final_score = calculate_final_score(
#         tfidf_score, bert_score, skill_score,
#         experience_score, title_score, cert_score, edu_score
#     )

#     return {
#         "final_score": final_score,
#         "tfidf_score": round(tfidf_score * 100, 2),
#         "bert_score": round(bert_score * 100, 2),
#         "skill_score": round(skill_score * 100, 2),
#         "experience_score": round(experience_score * 100, 2),
#         "title_score": round(title_score * 100, 2),
#         "matched_skills": matched_skills,
#         "missing_skills": missing_skills
#     }


# def rank_resumes(jd_text, resumes):
#     results = []
#     for resume in resumes:
#         match = match_resume_to_jd(jd_text, resume["text"])
#         results.append({
#             "name": resume["name"],
#             "email": resume["email"],
#             "file_name": resume["file_name"],
#             "final_score": match["final_score"],
#             "tfidf_score": match["tfidf_score"],
#             "bert_score": match["bert_score"],
#             "skill_score": match["skill_score"],
#             "experience_score": match["experience_score"],
#             "title_score": match["title_score"],
#             "matched_skills": match["matched_skills"],
#             "missing_skills": match["missing_skills"]
#         })
#     results.sort(key=lambda x: x["final_score"], reverse=True)
#     return results






from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from src.nlp import extract_skills
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

# ---------------------------
# EMBEDDING CACHE
# ---------------------------
skill_embedding_cache = {}

def get_embedding(skill):
    if skill not in skill_embedding_cache:
        skill_embedding_cache[skill] = model.encode(skill)
    return skill_embedding_cache[skill]

def semantic_skill_similarity(skill1, skill2):
    try:
        emb1 = get_embedding(skill1)
        emb2 = get_embedding(skill2)
        return cosine_similarity([emb1], [emb2])[0][0]
    except:
        return 0.0


# ---------------------------
# TF-IDF
# ---------------------------
def calculate_tfidf_score(jd_text, resume_text):
    try:
        vectorizer = TfidfVectorizer(stop_words='english')
        vectors = vectorizer.fit_transform([jd_text, resume_text])
        return cosine_similarity(vectors[0], vectors[1])[0][0]
    except:
        return 0.0


# ---------------------------
# BERT
# ---------------------------
def calculate_bert_score(jd_text, resume_text):
    try:
        emb = model.encode([jd_text, resume_text], show_progress_bar=False)
        return cosine_similarity([emb[0]], [emb[1]])[0][0]
    except:
        return 0.0


# ---------------------------
# EQUIVALENT SKILLS
# ---------------------------
EQUIVALENT_SKILLS = [
    {"spark", "pyspark", "apache spark"},
    {"kafka", "apache kafka"},
    {"airflow", "apache airflow"},
    {"hadoop", "apache hadoop"},
    {"postgres", "postgresql"},
    {"git", "github"},
    {"etl", "elt"},
    {"kubernetes", "k8s"},
    {"ci/cd", "jenkins", "cicd"},
    {"databricks", "delta lake"},
    {"ml", "machine learning", "ai/ml", "artificial intelligence"},
    {"redshift", "aws redshift"},
    {"bigquery", "google bigquery"},
]

SKILL_FAMILIES = {
    "data_engineering": ["etl", "elt", "data pipeline", "airflow"],
    "big_data": ["spark", "pyspark", "hadoop", "kafka"],
    "cloud": ["aws", "azure", "gcp"],
    "ml": ["ml", "ai", "machine learning", "ai/ml"],
    "data_storage": ["snowflake", "redshift", "bigquery", "databricks"]
}

def same_family(s1, s2):
    for family in SKILL_FAMILIES.values():
        if s1 in family and s2 in family:
            return True
    return False


# ---------------------------
# SKILL MATCH (SELF-LEARNING)
# ---------------------------
def skills_match_score(skill1, skill2):
    s1 = skill1.lower().strip()
    s2 = skill2.lower().strip()

    if s1 == s2:
        return 1.0

    if len(s1) > 3 and len(s2) > 3:
        if s1 in s2 or s2 in s1:
            return 0.9

    for group in EQUIVALENT_SKILLS:
        if s1 in group and s2 in group:
            return 0.75

    if same_family(s1, s2):
        return 0.6

    # semantic fallback (self-learning)
    sim = semantic_skill_similarity(s1, s2)

    if sim > 0.80:
        return 0.85
    elif sim > 0.65:
        return 0.7
    elif sim > 0.50:
        return 0.5

    return 0.0


# ---------------------------
# SKILL WEIGHTING
# ---------------------------
def get_skill_weight(skill):
    skill = skill.lower()

    core = ["python", "sql", "spark", "pyspark", "airflow", "kafka", "etl", "elt", "data modeling"]
    important = ["aws", "azure", "databricks", "docker", "kubernetes"]
    optional = ["sap", "salesforce", "workday", "snowflake", "bigquery",
                "redshift", "gcp", "pandas", "ai", "ml", "ai/ml", "data quality"]

    if any(k in skill for k in core):
        return 1.0
    elif any(k in skill for k in important):
        return 0.7
    elif any(k in skill for k in optional):
        return 0.3

    return 0.5


# ---------------------------
# SECTION SPLIT
# ---------------------------
def split_jd_sections(jd_text):
    jd = jd_text.lower()
    for delimiter in ["nice-to-have", "nice to have", "preferred qualifications", "good to have"]:
        if delimiter in jd:
            parts = jd.split(delimiter)
            return parts[0], parts[1]
    return jd, ""


# ---------------------------
# SKILL SCORE
# ---------------------------
def calculate_skill_score(jd_text, resume_text):
    try:
        required_text, preferred_text = split_jd_sections(jd_text)

        req_skills = list(set(extract_skills(required_text, required_text)))
        pref_skills = list(set(extract_skills(preferred_text, preferred_text))) if preferred_text else []
        resume_skills = list(set(extract_skills(resume_text, jd_text)))

        total_weight = 0
        matched_weight = 0
        missing = []
        matched_all = []

        for jd_skill in req_skills:
            weight = get_skill_weight(jd_skill)
            total_weight += weight

            best_score = max(
                [skills_match_score(jd_skill, rs) for rs in resume_skills],
                default=0
            )

            if best_score > 0:
                matched_weight += best_score * weight
                matched_all.append(jd_skill)
            else:
                missing.append(jd_skill)

        req_score = matched_weight / total_weight if total_weight else 0

        matched_pref = [
            skill for skill in pref_skills
            if any(skills_match_score(skill, rs) > 0 for rs in resume_skills)
        ]

        pref_score = len(matched_pref) / len(pref_skills) if pref_skills else 0

        final_skill_score = (0.85 * req_score) + (0.15 * pref_score)

        matched_all.extend(matched_pref)

        return round(final_skill_score, 4), matched_all, missing

    except Exception as e:
        print(f"Skill error: {e}")
        return 0.0, [], []


# ---------------------------
# EXPERIENCE
# ---------------------------
def calculate_experience_score(jd_text, resume_text):
    try:
        jd = jd_text.lower()
        res = resume_text.lower()

        jd_range = re.findall(r'(\d+)\s*[-to]+\s*(\d+)\s*years?', jd)
        res_years = re.findall(r'(\d+)\+?\s*years?', res)

        if not res_years:
            return 0.5

        candidate = max([int(x) for x in res_years if int(x) < 50])

        if jd_range:
            jd_min, jd_max = int(jd_range[0][0]), int(jd_range[0][1])
        else:
            return 0.6

        if jd_min <= candidate <= jd_max:
            return 1.0
        elif candidate > jd_max:
            return 0.9
        elif candidate >= jd_min - 2:
            return 0.7
        else:
            return 0.4

    except:
        return 0.5


# ---------------------------
# TITLE
# ---------------------------
def calculate_title_score(jd_text, resume_text):
    try:
        jd = jd_text.lower()
        res = resume_text.lower()

        roles = ["data engineer", "software engineer", "data scientist"]

        jd_role = next((r for r in roles if r in jd), None)
        res_role = next((r for r in roles if r in res), None)

        if not jd_role or not res_role:
            return 0.5

        if jd_role == res_role:
            return 1.0
        elif jd_role in res_role or res_role in jd_role:
            return 0.85
        else:
            return 0.4

    except:
        return 0.5


# ---------------------------
# FINAL SCORE
# ---------------------------
def calculate_final_score(tfidf, bert, skill, exp=0.5, title=0.5):
    return round((
        tfidf * 0.05 +
        bert * 0.35 +
        skill * 0.35 +
        exp * 0.15 +
        title * 0.10
    ) * 100, 2)


# ---------------------------
# MAIN
# ---------------------------
def match_resume_to_jd(jd_text, resume_text):
    tfidf = calculate_tfidf_score(jd_text, resume_text)
    bert = calculate_bert_score(jd_text, resume_text)
    skill, matched, missing = calculate_skill_score(jd_text, resume_text)
    exp = calculate_experience_score(jd_text, resume_text)
    title = calculate_title_score(jd_text, resume_text)

    final = calculate_final_score(tfidf, bert, skill, exp, title)

    return {
        "final_score": final,
        "tfidf_score": round(tfidf * 100, 2),
        "bert_score": round(bert * 100, 2),
        "skill_score": round(skill * 100, 2),
        "experience_score": round(exp * 100, 2),
        "title_score": round(title * 100, 2),
        "matched_skills": matched,
        "missing_skills": missing
    }


# ---------------------------
# RANKING
# ---------------------------
def rank_resumes(jd_text, resumes):
    results = []

    for resume in resumes:
        match = match_resume_to_jd(jd_text, resume["text"])

        results.append({
            "name": resume["name"],
            "email": resume["email"],
            "file_name": resume["file_name"],
            "final_score": match["final_score"],
            "tfidf_score": match["tfidf_score"],
            "bert_score": match["bert_score"],
            "skill_score": match["skill_score"],
            "experience_score": match["experience_score"],
            "title_score": match["title_score"],
            "matched_skills": match["matched_skills"],
            "missing_skills": match["missing_skills"]
        })

    results.sort(key=lambda x: x["final_score"], reverse=True)
    return results