# import spacy
# import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords', quiet=True)
# nltk.download('punkt', quiet=True)

# nlp = spacy.load("en_core_web_sm")

# SKILLS_DATABASE = [
#     # ── Languages ──
#     "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift",
#     "kotlin", "typescript", "matlab", "scala", "perl", "bash", "shell",
#     "r", "go", "julia", "rust", "groovy",

#     # ── Web & Frontend ──
#     "html", "css", "react", "angular", "vue", "node", "django", "flask",
#     "fastapi", "spring", "graphql", "rest api", "microservices",

#     # ── AI / ML / DL ──
#     "tensorflow", "pytorch", "keras", "scikit-learn", "opencv", "nltk", "spacy",
#     "machine learning", "deep learning", "nlp", "computer vision",
#     "artificial intelligence", "neural networks", "data science",
#     "ai", "ml", "ai/ml", "feature engineering", "model serving",
#     "llm", "generative ai", "transformers", "hugging face",

#     # ── Data Engineering ──
#     "spark", "pyspark", "apache spark",
#     "kafka", "apache kafka",
#     "airflow", "apache airflow",
#     "hadoop", "apache hadoop",
#     "hive", "hdfs", "emr", "glue", "s3",
#     "flink", "kafka streams",
#     "dbt", "etl", "elt",
#     "data pipeline", "data pipelines",
#     "data warehouse", "data lake", "data lakehouse",
#     "data modeling", "data engineering", "data integration",
#     "data quality", "batch processing", "streaming", "real time",

#     # ── Cloud Platforms ──
#     "aws", "azure", "gcp",
#     "google cloud", "amazon web services", "microsoft azure",
#     "cloud computing", "cloud native",

#     # ── Cloud Services ──
#     "databricks", "snowflake", "redshift", "bigquery",
#     "delta lake", "delta",
#     "dynamo", "hbase", "cassandra", "cosmos db",
#     "azure cosmos db", "azure blob",

#     # ── Databases ──
#     "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle", "redis",
#     "sqlalchemy", "impala", "sql server",

#     # ── DevOps & Infra ──
#     "docker", "kubernetes", "k8s",
#     "jenkins", "ci/cd", "cicd",
#     "terraform", "ansible",
#     "git", "github", "svn",
#     "linux", "devops",

#     # ── Data Analysis & BI ──
#     "pandas", "numpy", "matplotlib", "seaborn",
#     "data analysis", "data visualization",
#     "big data", "excel", "power bi", "tableau",

#     # ── Enterprise Systems ──
#     "sap", "sap abap", "abap", "oracle",
#     "salesforce", "workday", "servicenow",

#     # ── Methodology & Practices ──
#     "agile", "scrum", "data structures", "algorithms",
#     "object oriented", "unit testing", "code review",

#     # ── Other Tech ──
#     "blockchain", "iot", "cybersecurity",
#     "flutter", "react native", "android", "ios",
#     "selenium", "pytest", "junit", "postman",
#     "jira", "confluence",
#     "visual studio", "jupyter", "jupyter notebook",
#     "power automate", "ms office",
#     "solidity", "web3", "ethereum",
#     "computer networks", "operating systems",
# ]

# # Remove duplicates while preserving order
# seen = set()
# SKILLS_DATABASE = [
#     s for s in SKILLS_DATABASE
#     if not (s in seen or seen.add(s))
# ]

# SKILL_ALIASES = {
#     # Apache prefixed variants
#     "apache spark":   ["spark", "pyspark"],
#     "apache kafka":   ["kafka"],
#     "apache airflow": ["airflow"],
#     "apache hadoop":  ["hadoop"],

#     # Spark family
#     "spark":   ["pyspark", "apache spark"],
#     "pyspark": ["spark", "apache spark"],

#     # Cloud platforms
#     "aws":   ["amazon web services"],
#     "azure": ["microsoft azure"],
#     "gcp":   ["google cloud"],

#     # Databases
#     "postgresql":  ["postgres"],
#     "sql server":  ["mssql", "ms sql"],
#     "cosmos db":   ["azure cosmos db"],
#     "delta lake":  ["delta"],

#     # DevOps
#     "kubernetes": ["k8s"],
#     "ci/cd":      ["cicd", "jenkins"],

#     # ML libraries
#     "scikit-learn": ["sklearn"],
#     "tensorflow":   ["tf"],

#     # Languages & frameworks
#     "javascript": ["js"],
#     "typescript": ["ts"],
#     "react":      ["reactjs", "react.js"],
#     "node":       ["nodejs", "node.js"],
# }

# # Short skills that need exact word boundary matching to avoid false positives
# # e.g. "r" shouldn't match "error", "c" shouldn't match "science"
# EXACT_MATCH_SKILLS = ["r", "go", "c", "perl", "julia"]

# STOP_WORDS = set(stopwords.words('english'))

# COMMON_WORDS_TO_IGNORE = {
#     "education", "experience", "skills", "objective", "summary",
#     "projects", "certifications", "publications", "activities",
#     "leadership", "technical", "work", "profile", "contact",
#     "interests", "languages", "references", "achievements",
#     "responsibilities", "date", "name", "email", "phone",
#     "address", "linkedin", "github", "university", "college",
#     "institute", "school", "bachelor", "master", "degree"
# }

# def extract_skills(text, jd_text=None):
#     """
#     Fully JD-driven skill extraction.
    
#     If jd_text is provided (resume evaluation context):
#         - Extract skill candidates from JD
#         - Check which ones appear in the resume text
#         - No hardcoded database needed
    
#     If jd_text is not provided (extracting FROM the JD itself):
#         - Use NLP to pull noun phrases and technical terms
#         - Fall back to SKILLS_DATABASE as a supplementary boost only
#     """
#     import re
#     text_lower = text.lower()
#     found_skills = []

#     # ── Layer 1: If JD text provided, extract skills FROM JD and check resume ──
#     if jd_text:
#         jd_lower = jd_text.lower()
        
#         # Split JD into candidate skill tokens by common delimiters
#         candidates = re.split(r'[,\n•\-\|/\(\)]', jd_lower)
#         for candidate in candidates:
#             candidate = candidate.strip()
#             # Valid skill: 2-40 chars, not a stop word, not a common resume section word
#             if (2 <= len(candidate) <= 40
#                     and candidate not in STOP_WORDS
#                     and candidate not in COMMON_WORDS_TO_IGNORE
#                     and not candidate.isdigit()):
#                 # Check if this JD skill appears in the resume
#                 if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
#                     found_skills.append(candidate)

#     # ── Layer 2: SKILLS_DATABASE as supplementary boost ──
#     # Catches skills that may be phrased differently in JD but present in resume
#     for skill in SKILLS_DATABASE:
#         if skill not in found_skills:
#             pattern = r'\b' + re.escape(skill) + r'\b'
#             if re.search(pattern, text_lower):
#                 found_skills.append(skill)

#     return list(set(found_skills))

# def extract_education(text):
#     education_keywords = [
#         "bachelor", "master", "phd", "b.tech", "m.tech", "mba", "bca",
#         "mca", "b.sc", "m.sc", "degree", "diploma", "graduate",
#         "undergraduate", "university", "college", "institute", "school",
#         "cgpa", "gpa", "computer science", "engineering",
#         "information technology"
#     ]
#     doc = nlp(text)
#     education = []
#     sentences = [sent.text for sent in doc.sents]
#     for sentence in sentences:
#         sentence_lower = sentence.lower()
#         if any(keyword in sentence_lower for keyword in education_keywords):
#             education.append(sentence.strip())
#     return " | ".join(education[:3]) if education else "Not found"


# def extract_experience(text):
#     experience_patterns = [
#         r'\d+\+?\s*years?\s*of\s*experience',
#         r'experience\s*of\s*\d+\+?\s*years?',
#         r'\d+\+?\s*years?\s*experience',
#         r'worked\s*at\s*\w+',
#         r'internship\s*at\s*\w+',
#         r'intern\s*at\s*\w+',
#     ]
#     found_experience = []
#     for pattern in experience_patterns:
#         matches = re.findall(pattern, text.lower())
#         found_experience.extend(matches)
#     doc = nlp(text)
#     org_names = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
#     if org_names:
#         found_experience.append(
#             "Organizations: " + ", ".join(org_names[:3]))
#     return " | ".join(found_experience[:3]) if found_experience else "Not found"


# def extract_candidate_name(text):
#     # Try spaCy PERSON entity first
#     doc = nlp(text[:500])
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             name = ent.text.strip()
#             if 2 <= len(name.split()) <= 4:
#                 return name

#     # Try first non-empty line that looks like a name
#     lines = text.strip().split('\n')
#     for line in lines[:5]:
#         line = line.strip()
#         # Remove phone numbers, emails, special chars
#         cleaned = re.sub(r'[\d\+\-\(\)\@\.\,\|]', '', line).strip()
#         # A name is 2-4 words, all letters
#         words = cleaned.split()
#         if 2 <= len(words) <= 4:
#             if all(w.replace("'", "").isalpha() for w in words):
#                 return cleaned

#     # Try finding name near common resume keywords
#     name_pattern = r'^([A-Z][a-z]+(?:\s[A-Z][a-z]+){1,3})'
#     for line in lines[:8]:
#         match = re.match(name_pattern, line.strip())
#         if match:
#             return match.group(1)

#     # Fallback — use filename without extension
#     return "Candidate"


# def extract_candidate_email(text):
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     emails = re.findall(email_pattern, text)
#     return emails[0] if emails else "Not found"


# def process_resume(text, jd_text=None):
#     return {
#         "name": extract_candidate_name(text),
#         "email": extract_candidate_email(text),
#         "skills": extract_skills(text, jd_text),
#         "education": extract_education(text),
#         "experience": extract_experience(text)
#     }


# def process_jd(text):
#     required_skills = []
#     preferred_skills = []

#     text_lower = text.lower()

#     required_section = ""
#     preferred_section = ""

#     if "required" in text_lower:
#         parts = text_lower.split("required")
#         if len(parts) > 1:
#             required_section = parts[1][:500]

#     if "preferred" in text_lower or "nice to have" in text_lower:
#         split_word = "preferred" if "preferred" in text_lower else "nice to have"
#         parts = text_lower.split(split_word)
#         if len(parts) > 1:
#             preferred_section = parts[1][:500]

#     if required_section:
#         required_skills = extract_skills(required_section)
#     if preferred_section:
#         preferred_skills = extract_skills(preferred_section)

#     all_skills = extract_skills(text)

#     return {
#         "required_skills": required_skills if required_skills else all_skills,
#         "preferred_skills": preferred_skills,
#         "all_skills": all_skills,
#         "education": extract_education(text),
#         "experience": extract_experience(text)
#     }



import spacy
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

nlp = spacy.load("en_core_web_sm")

# ─────────────────────────────────────────────
# SKILLS DATABASE (Fallback Layer - Generalized)
# ─────────────────────────────────────────────
SKILLS_DATABASE = [
    "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift",
    "kotlin", "typescript", "matlab", "perl",
    "html", "css", "react", "angular", "vue", "node", "django", "flask",
    "spring", "tensorflow", "pytorch", "keras", "scikit-learn", "pandas",
    "numpy", "matplotlib", "seaborn", "opencv", "nltk", "spacy",
    "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle", "redis",
    "aws", "azure", "gcp", "docker", "kubernetes", "git", "github",
    "machine learning", "deep learning", "nlp", "computer vision",
    "data science", "artificial intelligence", "neural networks",
    "data analysis", "data visualization", "big data", "hadoop", "spark",
    "rest api", "graphql", "microservices", "agile", "scrum", "devops",
    "linux", "excel", "power bi", "tableau", "sap", "abap",
    "blockchain", "iot", "cloud computing", "cybersecurity",
    "flutter", "react native", "android", "ios",
    "selenium", "junit", "pytest", "postman", "jira", "confluence",
    "ai", "ml", "ai/ml", "data structures", "algorithms",
    "computer networks", "operating systems", "object oriented",
    "visual studio", "jupyter", "jupyter notebook",
    "kafka", "airflow", "pyspark", "scala",
    "databricks", "snowflake", "redshift", "bigquery",
    "delta lake", "dbt", "etl", "elt",
    "data pipeline", "data warehouse", "data lake",
    "data modeling", "data engineering", "data quality",
    "apache spark", "apache kafka", "apache airflow", "apache hadoop",
    "hive", "hdfs", "emr", "glue", "s3",
    "cosmos db", "cassandra", "dynamo",
    "jenkins", "ci/cd", "terraform", "ansible",
    "sqlalchemy", "salesforce", "workday", "servicenow",
    "streaming", "batch processing", "real time",
    "data integration", "sap abap", "qr code",
    "solidity", "web3", "ethereum",
    "power automate", "ms office",

    # Non-tech/general domain additions
    "accounting", "finance", "taxation", "auditing",
    "marketing", "sales", "customer service", "communication",
    "leadership", "management", "teaching", "research",
    "curriculum design", "lesson planning", "public speaking",
    "content writing", "copywriting", "seo", "social media",
    "graphic design", "photoshop", "illustrator", "figma"
]

EXACT_MATCH_SKILLS = ["r", "go", "c"]

STOP_WORDS = set(stopwords.words('english'))

SECTION_HEADERS = {
    "education", "experience", "skills", "objective", "summary",
    "projects", "certifications", "publications", "activities",
    "leadership", "technical", "work", "profile", "contact",
    "interests", "languages", "references", "achievements",
    "responsibilities", "date", "name", "email", "phone",
    "address", "linkedin", "github", "university", "college",
    "institute", "school", "bachelor", "master", "degree",
    "requirements", "qualifications", "nice to have",
    "preferred", "required", "key skills", "overview"
}

NOISE_WORDS = {
    "strong", "experience", "knowledge", "understanding", "familiarity",
    "proficiency", "ability", "skill", "skills", "proven",
    "years", "year", "months", "month",
    "good", "well", "excellent", "team", "working",
    "using", "including", "such", "etc", "based",
    "data", "systems", "platforms", "solutions",
    "environment", "process", "business"
}

def clean_phrase(candidate):
    words = candidate.split()

    # remove noise words inside phrase
    words = [
        w for w in words
        if w not in STOP_WORDS
        and w not in NOISE_WORDS
    ]

    # rebuild phrase
    candidate = " ".join(words)

    # final checks
    if len(candidate) < 2:
        return None

    if len(candidate.split()) > 3:
        return None

    return candidate

# ─────────────────────────────────────────────
# SKILL EXTRACTION (FINAL STABLE VERSION)
# ─────────────────────────────────────────────
def extract_skills(text, jd_text=None):
    text_lower = text.lower()
    found_skills = set()

    # ── STEP 1: JD-DRIVEN EXTRACTION ──
    if jd_text:
        jd_lower = jd_text.lower()
        candidates = re.split(r'[,\n•\-\|/\(\)\[\]]', jd_lower)

        for candidate in candidates:
            candidate = candidate.strip().lower()
            candidate = re.sub(r'\s+', ' ', candidate)

            candidate = clean_phrase(candidate)
            if candidate in {"and", "or", "with", "using"}:
                continue
            if not candidate:
                continue

            if not (2 <= len(candidate) <= 30):
                continue

            if len(candidate.split()) > 3:
                continue

            if any(char.isdigit() for char in candidate):
                continue

            if candidate in STOP_WORDS:
                continue
            if candidate in SECTION_HEADERS:
                continue
            if candidate in NOISE_WORDS:
                continue

            words = candidate.split()
            if all(w in STOP_WORDS or w in NOISE_WORDS for w in words):
                continue

            if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
                found_skills.add(candidate)

    # ── STEP 2: SKILL DATABASE SUPPORT ──
    for skill in SKILLS_DATABASE:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)

    # ── STEP 3: EXACT MATCH SHORT SKILLS ──
    for skill in EXACT_MATCH_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text_lower):
            found_skills.add(skill)

    return list(set(found_skills))


# ─────────────────────────────────────────────
# EDUCATION
# ─────────────────────────────────────────────
def extract_education(text):
    keywords = [
        "bachelor", "master", "phd", "b.tech", "m.tech",
        "mba", "bca", "mca", "b.sc", "m.sc", "degree"
    ]

    doc = nlp(text)
    education = []

    for sent in doc.sents:
        if any(k in sent.text.lower() for k in keywords):
            education.append(sent.text.strip())

    return " | ".join(education[:3]) if education else "Not found"


# ─────────────────────────────────────────────
# EXPERIENCE
# ─────────────────────────────────────────────
def extract_experience(text):
    patterns = [
        r'\d+\+?\s*years?\s*experience',
        r'experience\s*of\s*\d+\+?\s*years?',
        r'\d+\+?\s*years?\s*of\s*experience'
    ]

    found = []

    for pattern in patterns:
        found.extend(re.findall(pattern, text.lower()))

    return " | ".join(found[:3]) if found else "Not found"


# ─────────────────────────────────────────────
# NAME
# ─────────────────────────────────────────────
def extract_candidate_name(text):
    doc = nlp(text[:500])

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()

    lines = text.strip().split('\n')
    for line in lines[:5]:
        words = line.strip().split()
        if 2 <= len(words) <= 4:
            return line.strip()

    return "Candidate"


# ─────────────────────────────────────────────
# EMAIL
# ─────────────────────────────────────────────
def extract_candidate_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails[0] if emails else "Not found"


# ─────────────────────────────────────────────
# PROCESS FUNCTIONS
# ─────────────────────────────────────────────
def process_resume(text, jd_text=None):
    return {
        "name": extract_candidate_name(text),
        "email": extract_candidate_email(text),
        "skills": extract_skills(text, jd_text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }


def process_jd(text):
    return {
        "required_skills": extract_skills(text),
        "education": extract_education(text),
        "experience": extract_experience(text)
    }