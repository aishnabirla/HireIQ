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


# # def extract_skills(text, jd_text=None):
# #     text_lower = text.lower()
# #     found_skills = []

# #     for skill in SKILLS_DATABASE:
# #         if len(skill) > 3:
# #             if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
# #                 found_skills.append(skill)
# #         else:
# #             pattern = r'\b' + re.escape(skill) + r'\b'
# #             if re.search(pattern, text_lower):
# #                 found_skills.append(skill)

# #     for skill in EXACT_MATCH_SKILLS:
# #         pattern = r'\b' + re.escape(skill) + r'\b'
# #         if re.search(pattern, text_lower):
# #             found_skills.append(skill)

# #     if jd_text:
# #         jd_lower = jd_text.lower()
# #         items = re.split(r'[,\n•\-\|/]', jd_lower)
# #         for item in items:
# #             item = item.strip()
# #             if (2 < len(item) < 25
# #                     and item not in STOP_WORDS
# #                     and item not in COMMON_WORDS_TO_IGNORE
# #                     and item in text_lower
# #                     and item not in found_skills):
# #                 found_skills.append(item)

# #     return list(set(found_skills))

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






# import spacy
# import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords', quiet=True)
# nltk.download('punkt', quiet=True)

# nlp = spacy.load("en_core_web_sm")

# SKILLS_DATABASE = [
#     "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift",
#     "kotlin", "typescript", "matlab", "perl",
#     "html", "css", "react", "angular", "vue", "node", "django", "flask",
#     "spring", "tensorflow", "pytorch", "keras", "scikit-learn", "pandas",
#     "numpy", "matplotlib", "seaborn", "opencv", "nltk", "spacy",
#     "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle", "redis",
#     "aws", "azure", "gcp", "docker", "kubernetes", "git", "github",
#     "machine learning", "deep learning", "nlp", "computer vision",
#     "data science", "artificial intelligence", "neural networks",
#     "data analysis", "data visualization", "big data", "hadoop", "spark",
#     "rest api", "graphql", "microservices", "agile", "scrum", "devops",
#     "linux", "excel", "power bi", "tableau", "sap", "abap",
#     "blockchain", "iot", "cloud computing", "cybersecurity",
#     "flutter", "react native", "android", "ios",
#     "selenium", "junit", "pytest", "postman", "jira", "confluence",
#     "ai", "ml", "ai/ml", "data structures", "algorithms",
#     "computer networks", "operating systems", "object oriented",
#     "visual studio", "jupyter", "jupyter notebook",
#     "kafka", "airflow", "pyspark", "scala",
#     "databricks", "snowflake", "redshift", "bigquery",
#     "delta lake", "dbt", "etl", "elt",
#     "data pipeline", "data warehouse", "data lake",
#     "data modeling", "data engineering", "data quality",
#     "apache spark", "apache kafka", "apache airflow", "apache hadoop",
#     "hive", "hdfs", "emr", "glue", "s3",
#     "cosmos db", "cassandra", "dynamo",
#     "jenkins", "ci/cd", "terraform", "ansible",
#     "sqlalchemy", "salesforce", "workday", "servicenow",
#     "streaming", "batch processing", "real time",
#     "data integration", "sap abap", "qr code",
#     "solidity", "web3", "ethereum",
#     "power automate", "ms office"
# ]

# EXACT_MATCH_SKILLS = ["r", "go", "c", "perl", "julia"]

# STOP_WORDS = set(stopwords.words('english'))

# SECTION_HEADERS = {
#     "education", "experience", "skills", "objective", "summary",
#     "projects", "certifications", "publications", "activities",
#     "leadership", "technical", "work", "profile", "contact",
#     "interests", "languages", "references", "achievements",
#     "responsibilities", "date", "name", "email", "phone",
#     "address", "linkedin", "github", "university", "college",
#     "institute", "school", "bachelor", "master", "degree",
#     "requirements", "qualifications", "responsibilities",
#     "nice to have", "preferred", "required", "key skills",
#     "key responsibilities", "about", "overview"
# }

# NOISE_WORDS = {
#     "strong", "experience", "knowledge", "understanding", "familiarity",
#     "proficiency", "ability", "skill", "skills", "proven", "hands",
#     "years", "year", "months", "month", "level", "senior", "junior",
#     "mid", "lead", "manager", "engineer", "developer", "analyst",
#     "working", "using", "including", "such", "etc", "good", "well",
#     "excellent", "great", "team", "player", "ability", "including",
#     "least", "plus", "highly", "preferred", "required", "must",
#     "nice", "have", "bonus", "advantage", "desirable",
#     "tools", "data", "solutions", "platforms", "cloud",
#     "systems", "services", "applications", "environment",
#     "process", "processes", "business", "company", "organization",
#     "across", "within", "through", "various", "multiple",
#     "following", "above", "below", "per", "via", "based"
# }


# def extract_skills(text, jd_text=None):
#     text_lower = text.lower()
#     found_skills = set()

#     if jd_text:
#         jd_lower = jd_text.lower()
#         candidates = re.split(r'[,\n•\-\|/\(\)\[\]]', jd_lower)
#         for candidate in candidates:
#             candidate = candidate.strip()
#             candidate = re.sub(r'\s+', ' ', candidate)
#             if not (2 <= len(candidate) <= 35):
#                 continue
#             if candidate.isdigit():
#                 continue
#             if candidate in STOP_WORDS:
#                 continue
#             if candidate in SECTION_HEADERS:
#                 continue
#             if candidate in NOISE_WORDS:
#                 continue
#             words = candidate.split()
#             if all(w in NOISE_WORDS or w in STOP_WORDS for w in words):
#                 continue
#             if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
#                 found_skills.add(candidate)

#     for skill in SKILLS_DATABASE:
#         if skill not in found_skills:
#             pattern = r'\b' + re.escape(skill) + r'\b'
#             if re.search(pattern, text_lower):
#                 found_skills.add(skill)

#     for skill in EXACT_MATCH_SKILLS:
#         pattern = r'\b' + re.escape(skill) + r'\b'
#         if re.search(pattern, text_lower):
#             found_skills.add(skill)

#     return list(found_skills)


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
#             "Organizations: " + ", ".join(org_names[:3])
#         )
#     return " | ".join(found_experience[:3]) if found_experience else "Not found"


# def extract_candidate_name(text):
#     doc = nlp(text[:500])
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             name = ent.text.strip()
#             if 2 <= len(name.split()) <= 4:
#                 return name
#     lines = text.strip().split('\n')
#     for line in lines[:5]:
#         line = line.strip()
#         cleaned = re.sub(r'[\d\+\-\(\)\@\.\,\|]', '', line).strip()
#         words = cleaned.split()
#         if 2 <= len(words) <= 4:
#             if all(w.replace("'", "").isalpha() for w in words):
#                 return cleaned
#     name_pattern = r'^([A-Z][a-z]+(?:\s[A-Z][a-z]+){1,3})'
#     for line in lines[:8]:
#         match = re.match(name_pattern, line.strip())
#         if match:
#             return match.group(1)
#     return "Candidate"


# def extract_candidate_email(text):
#     email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     emails = re.findall(email_pattern, text)
#     return emails[0] if emails else "Not provided"


# def process_resume(text, jd_text=None):
#     return {
#         "name": extract_candidate_name(text),
#         "email": extract_candidate_email(text),
#         "skills": extract_skills(text, jd_text),
#         "education": extract_education(text),
#         "experience": extract_experience(text)
#     }


# def process_jd(text):
#     return {
#         "required_skills": extract_skills(text),
#         "education": extract_education(text),
#         "experience": extract_experience(text)
#     }






# import spacy
# import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download('stopwords', quiet=True)
# nltk.download('punkt', quiet=True)

# nlp = spacy.load("en_core_web_sm")

# # ─────────────────────────────────────────────
# #  SKILLS DATABASE
# #  Fallback layer — covers common skills across
# #  all domains. JD-driven extraction is primary.
# # ─────────────────────────────────────────────
# SKILLS_DATABASE = [
#     # ── Programming Languages ──
#     "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift",
#     "kotlin", "typescript", "matlab", "scala", "bash", "shell",
#     "rust", "groovy", "go", "r",

#     # ── Web & Frontend ──
#     "html", "css", "react", "angular", "vue", "node", "django", "flask",
#     "fastapi", "spring", "graphql", "rest api", "microservices",

#     # ── AI / ML / DL ──
#     "tensorflow", "pytorch", "keras", "scikit-learn", "opencv",
#     "machine learning", "deep learning", "nlp", "computer vision",
#     "artificial intelligence", "neural networks", "data science",
#     "feature engineering", "model serving", "llm", "generative ai",
#     "transformers", "hugging face", "mlops", "mlflow",

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
#     "data quality", "batch processing", "streaming",
#     "delta lake", "delta live tables",

#     # ── Cloud Platforms ──
#     "aws", "azure", "gcp",
#     "google cloud", "amazon web services", "microsoft azure",
#     "cloud computing", "cloud native",

#     # ── Cloud Services & Data Warehouses ──
#     "databricks", "snowflake", "redshift", "bigquery",
#     "delta", "dynamo", "hbase", "cassandra", "cosmos db",
#     "azure cosmos db", "azure blob", "azure data factory",
#     "azure synapse", "azure synapse analytics",
#     "azure data lake", "azure devops",
#     "aws glue", "aws s3", "aws ec2", "aws lambda",
#     "amazon redshift", "amazon aurora",

#     # ── Databases ──
#     "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle",
#     "redis", "sqlalchemy", "impala", "sql server", "teradata",
#     "neo4j",

#     # ── DevOps & Infrastructure ──
#     "docker", "kubernetes", "k8s",
#     "jenkins", "ci/cd", "cicd",
#     "terraform", "ansible",
#     "git", "github", "svn", "github actions",
#     "linux", "devops", "argo cd", "helm",

#     # ── Data Analysis & BI ──
#     "pandas", "numpy", "matplotlib", "seaborn",
#     "data analysis", "data visualization",
#     "big data", "excel", "power bi", "tableau",

#     # ── Enterprise Systems ──
#     "sap", "sap abap", "abap",
#     "salesforce", "workday", "servicenow",

#     # ── Design & Creative ──
#     "figma", "adobe xd", "sketch", "illustrator", "photoshop",
#     "canva", "indesign", "after effects", "premiere pro",
#     "ui design", "ux design", "wireframing", "prototyping",
#     "user research", "design thinking",

#     # ── Marketing ──
#     "seo", "sem", "google ads", "content writing", "copywriting",
#     "social media", "google analytics", "hubspot", "wordpress",

#     # ── Project Management ──
#     "agile", "scrum", "kanban", "jira", "confluence",
#     "project management", "product management",

#     # ── Finance ──
#     "financial modeling", "accounting", "taxation",
#     "financial analysis", "budgeting", "forecasting",

#     # ── Teaching ──
#     "curriculum design", "lesson planning", "classroom management",
#     "pedagogy", "e-learning", "lms", "instructional design",

#     # ── General Engineering ──
#     "data structures", "algorithms", "object oriented",
#     "unit testing", "code review", "system design",
#     "computer networks", "operating systems",

#     # ── Other Tech ──
#     "blockchain", "iot", "cybersecurity",
#     "flutter", "react native", "android", "ios",
#     "selenium", "pytest", "junit", "postman",
#     "visual studio", "jupyter", "jupyter notebook",
#     "power automate", "ms office",
#     "solidity", "web3", "ethereum",
#     "langchain", "openai", "fastapi",
# ]

# # Deduplicate while preserving order
# _seen = set()
# SKILLS_DATABASE = [
#     s for s in SKILLS_DATABASE
#     if not (_seen.add(s) or s in _seen)
# ]

# STOP_WORDS = set(stopwords.words('english'))

# # ─────────────────────────────────────────────
# #  SECTION HEADERS
# #  Only used to filter Layer 2 JD extraction
# # ─────────────────────────────────────────────
# SECTION_HEADERS = {
#     "objective", "summary", "projects", "certifications",
#     "publications", "activities", "contact", "interests",
#     "references", "profile", "overview", "about",
#     "key skills", "key responsibilities",
#     "nice to have", "required", "preferred",
# }

# # ─────────────────────────────────────────────
# #  NOISE WORDS
# #  Generic words that slip through JD splitting
# #  but are not actual skill names
# # ─────────────────────────────────────────────
# NOISE_WORDS = {
#     "proven", "strong", "solid", "hands-on", "advanced", "proficient",
#     "excellent", "good", "great", "effective", "efficient", "robust",
#     "modern", "scalable", "production", "enterprise", "native", "based",
#     "driven", "oriented", "grade", "level", "senior", "junior", "lead",
#     "principal", "mid", "entry",
#     "including", "using", "leveraging", "building", "developing",
#     "designing", "managing", "leading", "working", "writing",
#     "understanding", "ensuring", "implementing", "optimizing",
#     "collaborating", "maintaining", "creating", "delivering",
#     "proficiency", "familiarity", "knowledge", "ability",
#     "tools", "practices", "frameworks", "platforms",
#     "systems", "solutions", "services", "concepts", "principles",
#     "methodologies", "technologies", "languages", "libraries",
#     "environments", "applications", "processes", "pipelines",
#     "such", "similar", "other", "various", "multiple", "related",
#     "high", "real", "time", "end", "large", "well", "cross",
#     "full", "back", "front", "open", "source",
#     "years", "year", "months", "month",
# }

# # ─────────────────────────────────────────────
# #  FAKE ORG WORDS
# #  spaCy incorrectly tags these as ORG entities
# # ─────────────────────────────────────────────
# FAKE_ORG_WORDS = {
#     # Tech tools
#     "spark", "python", "java", "sql", "hadoop", "kafka",
#     "airflow", "databricks", "snowflake", "docker", "kubernetes",
#     "git", "linux", "scala", "pyspark", "tensorflow", "pytorch",
#     # Domain words
#     "healthcare", "retail", "finance", "banking", "insurance",
#     "telecom", "technology", "cloud", "server", "database",
#     "big data", "etl", "elt", "api", "ml", "ai",
#     # Job titles
#     "data engineer", "software engineer", "data scientist",
#     "developer", "analyst", "engineer", "manager", "lead",
#     "senior", "junior", "intern", "associate", "consultant",
#     # Generic
#     "mobile", "platform", "solution", "global", "services",
#     "systems", "group", "team", "client", "project",
# }

# # ─────────────────────────────────────────────
# #  JOB TITLE WORDS
# #  Used to strip title from name candidates
# # ─────────────────────────────────────────────
# JOB_TITLE_WORDS = {
#     "engineer", "developer", "analyst", "scientist", "manager",
#     "lead", "architect", "consultant", "specialist", "director",
#     "officer", "intern", "associate", "senior", "junior", "head",
#     "vp", "president", "executive", "contact", "profile", "resume",
#     "cv", "data", "software", "cloud", "solutions", "technical",
#     "ai", "ml", "full", "stack", "backend", "frontend",
# }


# # ─────────────────────────────────────────────
# #  NAME NORMALISATION HELPERS
# # ─────────────────────────────────────────────
# def _clean_name_line(line):
#     """
#     Strips common prefixes like 'NAME:', 'Name:',
#     phone numbers, emails, and special chars from a line.
#     """
#     # Remove label prefixes like "NAME:", "Name :"
#     line = re.sub(r'^(?:name\s*[:\-]\s*)', '', line.strip(), flags=re.IGNORECASE)
#     # Remove emails
#     line = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', line)
#     # Remove phone numbers
#     line = re.sub(r'[\+\d\-\(\)\s]{7,}', ' ', line)
#     # Remove special chars except spaces and apostrophes
#     line = re.sub(r'[^\w\s\']', ' ', line)
#     line = re.sub(r'\s+', ' ', line).strip()
#     return line


# def _is_valid_name(words):
#     """
#     Returns True if word list looks like a real name:
#     - 2-3 words
#     - All alphabetic
#     - No job title words
#     - No single-character words except initials (handled separately)
#     """
#     if not (2 <= len(words) <= 3):
#         return False
#     if not all(w.replace("'", "").isalpha() for w in words):
#         return False
#     if any(w.lower() in JOB_TITLE_WORDS for w in words):
#         return False
#     return True


# def _normalise_spaced_name(text):
#     """
#     Handles spaced-out names like 'M O H A M M E D F A R I D H'
#     by detecting sequences of single letters separated by spaces
#     and collapsing them into a word.
#     """
#     # Pattern: 2+ single uppercase letters separated by spaces
#     spaced = re.findall(r'(?:[A-Z]\s){2,}[A-Z]', text)
#     result = text
#     for match in spaced:
#         collapsed = match.replace(' ', '')
#         result = result.replace(match, collapsed + ' ')
#     return result.strip()


# # ─────────────────────────────────────────────
# #  NAME EXTRACTION
# #  Handles:
# #  - All-caps names: LAKSHAY GOEL, ANKIT JAIN
# #  - Spaced names: M O H A M M E D F A R I D H
# #  - Name with prefix: NAME: Singam Vivek Kumar
# #  - Name + title on same line: Lakshay Goel Data Engineer
# #  - Short surname: Gangadhar K
# # ─────────────────────────────────────────────
# def extract_candidate_name(text):
#     # Pre-process: collapse spaced-out names
#     text_normalised = _normalise_spaced_name(text)
#     lines = text_normalised.strip().split('\n')

#     # ── Strategy 1: spaCy PERSON on first 400 chars ──
#     # Works for clean single-column resumes with proper casing
#     doc = nlp(text_normalised[:400])
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             words = ent.text.strip().split()
#             if _is_valid_name(words):
#                 return ' '.join(w.capitalize() for w in words)

#     # ── Strategy 2: Line-by-line scan ──
#     for line in lines[:8]:
#         # Clean the line
#         cleaned = _clean_name_line(line)
#         if not cleaned:
#             continue

#         # Normalise casing — handle ALL-CAPS names
#         # "LAKSHAY GOEL" → "Lakshay Goel"
#         if cleaned.isupper():
#             cleaned = cleaned.title()

#         words = cleaned.split()

#         # Exact 2-3 word name
#         if _is_valid_name(words):
#             return cleaned

#         # 4-word line — try stripping last word if it's a title word
#         # handles "Lakshay Goel Data Engineer" → "Lakshay Goel"
#         if len(words) == 4:
#             if words[-1].lower() in JOB_TITLE_WORDS:
#                 candidate = words[:3]
#                 if _is_valid_name(candidate):
#                     return ' '.join(candidate)
#             # Also try first 2 words
#             if words[2].lower() in JOB_TITLE_WORDS:
#                 candidate = words[:2]
#                 if _is_valid_name(candidate):
#                     return ' '.join(candidate)

#         # Handle "Gangadhar K" — 2 words where second is single initial
#         if len(words) == 2:
#             if (len(words[1]) == 1 and words[1].isalpha()
#                     and words[0].replace("'", "").isalpha()
#                     and words[0].lower() not in JOB_TITLE_WORDS):
#                 name = words[0].capitalize() + ' ' + words[1].upper()
#                 return name

#     # ── Strategy 3: Regex — Title Case or ALL CAPS name ──
#     # Matches "Radhey Shyam" or "RADHEY SHYAM"
#     patterns = [
#         r'^([A-Z][a-z]+(?:\s[A-Z][a-z]+){1,2})$',   # Title Case
#         r'^([A-Z]{2,}(?:\s[A-Z]{2,}){1,2})$',        # ALL CAPS
#     ]
#     for line in lines[:8]:
#         cleaned = _clean_name_line(line).strip()
#         for pattern in patterns:
#             match = re.match(pattern, cleaned)
#             if match:
#                 name = match.group(1).title()
#                 words = name.split()
#                 if _is_valid_name(words):
#                     return name

#     return "Candidate"


# # ─────────────────────────────────────────────
# #  EMAIL EXTRACTION
# # ─────────────────────────────────────────────
# def extract_candidate_email(text):
#     pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
#     emails = re.findall(pattern, text)
#     return emails[0] if emails else "Not provided"


# # ─────────────────────────────────────────────
# #  EDUCATION EXTRACTION
# #  Fixed: requires degree keyword AND institution
# #  keyword in the same sentence to avoid matching
# #  skills sections that contain "engineering"
# # ─────────────────────────────────────────────
# def extract_education(text):
#     degree_keywords = [
#         "bachelor", "master", "phd", "ph.d", "b.tech", "m.tech",
#         "mba", "bca", "mca", "b.sc", "m.sc", "b.e", "m.e",
#         "degree", "diploma", "graduate", "undergraduate",
#         "b.com", "m.com", "msc", "m.s", "b.s", "be", "btech",
#         "bachelor of", "master of", "doctor of",
#     ]
#     institution_keywords = [
#         "university", "college", "institute", "school",
#         "institution", "academy", "iit", "nit", "bits",
#         "iim", "anna university", "osmania", "kurukshetra",
#         "liverpool", "newcastle", "jntuh", "makaut",
#     ]
#     score_keywords = [
#         "cgpa", "gpa", "percentage", "%", "distinction",
#         "first class", "second class",
#     ]

#     doc = nlp(text)
#     education = []

#     for sent in doc.sents:
#         sent_lower = sent.text.lower()
#         has_degree      = any(kw in sent_lower for kw in degree_keywords)
#         has_institution = any(kw in sent_lower for kw in institution_keywords)
#         has_score       = any(kw in sent_lower for kw in score_keywords)

#         # Require degree + (institution OR score) to qualify
#         if has_degree and (has_institution or has_score):
#             education.append(sent.text.strip())

#     # Fallback: look for education section explicitly
#     if not education:
#         edu_section = re.search(
#             r'(?:education|qualification)[s]?\s*[:\-]?\s*\n(.*?)(?:\n\n|\Z)',
#             text,
#             re.IGNORECASE | re.DOTALL
#         )
#         if edu_section:
#             education.append(edu_section.group(1).strip()[:200])

#     return " | ".join(education[:3]) if education else "Not found"


# # ─────────────────────────────────────────────
# #  EXPERIENCE EXTRACTION
# #  Fixed:
# #  - Filters spaCy ORG false positives using
# #    FAKE_ORG_WORDS
# #  - Requires orgs to be multi-word OR well-known
# #    company-like names (Title Case, 4+ chars)
# #  - Deduplicates organisations
# # ─────────────────────────────────────────────
# def extract_experience(text):
#     found = []

#     # Years of experience — try patterns in order, stop at first match
#     year_patterns = [
#         r'\d+\+?\s*years?\s*of\s*(?:professional\s*)?experience',
#         r'experience\s*of\s*\d+\+?\s*years?',
#         r'\d+\+?\s*years?\s*experience',
#         r'\d+\+\s*years?',
#     ]
#     for pattern in year_patterns:
#         matches = re.findall(pattern, text.lower())
#         if matches:
#             found.extend(matches[:1])  # Take only first match to avoid duplicates
#             break

#     # Organisation extraction
#     doc = nlp(text)
#     real_orgs = []
#     seen_lower = set()

#     for ent in doc.ents:
#         if ent.label_ != "ORG":
#             continue

#         org = ent.text.strip()
#         org_lower = org.lower()

#         # Skip duplicates
#         if org_lower in seen_lower:
#             continue

#         # Skip single chars or very short orgs
#         if len(org) < 3:
#             continue

#         # Skip if it's a known fake org word
#         if org_lower in FAKE_ORG_WORDS:
#             continue

#         # Skip if it contains commas or slashes — likely a tech stack
#         if ',' in org or '/' in org:
#             continue

#         # Skip if any word in org matches fake org words
#         org_words = org_lower.split()
#         if any(w in FAKE_ORG_WORDS for w in org_words):
#             continue

#         # Skip if it's all lowercase — likely not a proper name
#         if org == org.lower():
#             continue

#         # Skip if it's all digits
#         if org.isdigit():
#             continue

#         real_orgs.append(org)
#         seen_lower.add(org_lower)

#     if real_orgs:
#         found.append("Organizations: " + ", ".join(real_orgs[:4]))

#     return " | ".join(found[:3]) if found else "Not found"


# # ─────────────────────────────────────────────
# #  SKILL EXTRACTION
# #  Layer 1 (PRIMARY): JD-driven — works for any domain
# #  Layer 2 (FALLBACK): SKILLS_DATABASE
# # ─────────────────────────────────────────────
# def extract_skills(text, jd_text=None):
#     text_lower = text.lower()
#     found_skills = set()

#     # ── Layer 1: JD-driven dynamic extraction ──
#     if jd_text:
#         jd_lower = jd_text.lower()
#         candidates = re.split(r'[,\n•\-\|/\(\)\[\]]', jd_lower)

#         for candidate in candidates:
#             candidate = candidate.strip()
#             candidate = re.sub(r'\s+', ' ', candidate)

#             if not (2 <= len(candidate) <= 25):
#                 continue
#             if len(candidate.split()) > 3:
#                 continue
#             if any(ch.isdigit() for ch in candidate):
#                 continue
#             if ':' in candidate:
#                 continue
#             if candidate in STOP_WORDS:
#                 continue
#             if candidate in SECTION_HEADERS:
#                 continue
#             if candidate in NOISE_WORDS:
#                 continue
#             words = candidate.split()
#             if all(w in NOISE_WORDS or w in STOP_WORDS for w in words):
#                 continue
#             if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
#                 found_skills.add(candidate)

#     # ── Layer 2: SKILLS_DATABASE fallback ──
#     for skill in SKILLS_DATABASE:
#         if skill not in found_skills:
#             pattern = r'\b' + re.escape(skill) + r'\b'
#             if re.search(pattern, text_lower):
#                 found_skills.add(skill)

#     return list(found_skills)


# # ─────────────────────────────────────────────
# #  PROCESS RESUME
# # ─────────────────────────────────────────────
# def process_resume(text, jd_text=None):
#     return {
#         "name":       extract_candidate_name(text),
#         "email":      extract_candidate_email(text),
#         "skills":     extract_skills(text, jd_text),
#         "education":  extract_education(text),
#         "experience": extract_experience(text)
#     }


# # ─────────────────────────────────────────────
# #  PROCESS JD
# # ─────────────────────────────────────────────
# def process_jd(text):
#     return {
#         "all_skills":  extract_skills(text, text),
#         "education":   extract_education(text),
#         "experience":  extract_experience(text)
#     }





import spacy
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

nlp = spacy.load("en_core_web_sm")

# ─────────────────────────────────────────────
#  SKILLS DATABASE — fallback layer only
#  JD-driven extraction (Layer 1) is primary.
#  This only catches skills phrased differently
#  in JD vs resume (e.g. JD: "Apache Spark",
#  resume: "Spark").
# ─────────────────────────────────────────────
SKILLS_DATABASE = [
    # ── Programming Languages ──
    "python", "java", "javascript", "c++", "c#", "ruby", "php", "swift",
    "kotlin", "typescript", "matlab", "scala", "bash", "shell",
    "rust", "groovy",

    # ── Web & Frontend ──
    "html", "css", "react", "angular", "vue", "node", "django", "flask",
    "fastapi", "spring", "graphql", "rest api", "microservices",

    # ── AI / ML / DL ──
    "tensorflow", "pytorch", "keras", "scikit-learn", "opencv",
    "machine learning", "deep learning", "nlp", "computer vision",
    "artificial intelligence", "neural networks", "data science",
    "feature engineering", "model serving", "llm", "generative ai",
    "transformers", "hugging face", "mlops", "mlflow",

    # ── Data Engineering ──
    "spark", "pyspark", "apache spark",
    "kafka", "apache kafka",
    "airflow", "apache airflow",
    "hadoop", "apache hadoop",
    "hive", "hdfs", "emr", "glue", "s3",
    "flink", "kafka streams",
    "dbt", "etl", "elt",
    "data pipeline", "data pipelines",
    "data warehouse", "data lake", "data lakehouse",
    "data modeling", "data engineering", "data integration",
    "data quality", "batch processing", "streaming",
    "delta lake", "delta live tables",

    # ── Cloud Platforms ──
    "aws", "azure", "gcp",
    "google cloud", "amazon web services", "microsoft azure",
    "cloud computing", "cloud native",

    # ── Cloud Services & Data Warehouses ──
    "databricks", "snowflake", "redshift", "bigquery",
    "delta", "dynamo", "hbase", "cassandra", "cosmos db",
    "azure cosmos db", "azure blob", "azure data factory",
    "azure synapse", "azure synapse analytics",
    "azure data lake", "azure devops",
    "aws glue", "amazon redshift", "amazon aurora",

    # ── Databases ──
    "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle",
    "redis", "sqlalchemy", "impala", "sql server", "teradata", "neo4j",

    # ── DevOps & Infrastructure ──
    "docker", "kubernetes", "k8s",
    "jenkins", "ci/cd", "cicd",
    "terraform", "ansible",
    "git", "github", "svn", "github actions",
    "linux", "devops", "argo cd", "helm",

    # ── Data Analysis & BI ──
    "pandas", "numpy", "matplotlib", "seaborn",
    "data analysis", "data visualization",
    "big data", "excel", "power bi", "tableau",

    # ── Enterprise Systems ──
    "sap", "sap abap", "abap",
    "salesforce", "workday", "servicenow",

    # ── Design & Creative ──
    "figma", "adobe xd", "sketch", "illustrator", "photoshop",
    "canva", "indesign", "after effects", "premiere pro",
    "ui design", "ux design", "wireframing", "prototyping",
    "user research", "design thinking",

    # ── Marketing ──
    "seo", "sem", "google ads", "content writing", "copywriting",
    "social media", "google analytics", "hubspot", "wordpress",

    # ── Project Management ──
    "agile", "scrum", "kanban", "jira", "confluence",
    "project management", "product management",

    # ── Finance ──
    "financial modeling", "accounting", "taxation",
    "financial analysis", "budgeting", "forecasting",

    # ── Teaching ──
    "curriculum design", "lesson planning", "classroom management",
    "pedagogy", "e-learning", "lms", "instructional design",

    # ── General Engineering ──
    "data structures", "algorithms", "object oriented",
    "unit testing", "code review", "system design",
    "computer networks", "operating systems",

    # ── Other Tech ──
    "blockchain", "iot", "cybersecurity",
    "flutter", "react native", "android", "ios",
    "selenium", "pytest", "junit", "postman",
    "visual studio", "jupyter", "jupyter notebook",
    "power automate", "ms office",
    "solidity", "web3", "ethereum",
    "langchain", "openai",
]

# Deduplicate while preserving order
_seen = set()
SKILLS_DATABASE = [
    s for s in SKILLS_DATABASE
    if not (_seen.add(s) or s in _seen)
]

STOP_WORDS = set(stopwords.words('english'))

# ─────────────────────────────────────────────
#  NOISE WORDS
#  Words that slip through JD delimiter-based
#  splitting but are NOT skill names.
#  Fixed: added all words leaking in test output:
#  'code', 'data', 'cloud', 'design', 'hands',
#  'ci', 'cd', 'reliability', 'reviews',
#  'reusable', 'develop', 'and cloud', 'and cost'
# ─────────────────────────────────────────────
NOISE_WORDS = {
    # Qualifiers
    "proven", "strong", "solid", "hands-on", "hands", "advanced",
    "proficient", "excellent", "good", "great", "effective",
    "efficient", "robust", "modern", "scalable", "production",
    "enterprise", "native", "based", "driven", "oriented",
    "grade", "level", "senior", "junior", "lead", "principal",
    "mid", "entry", "real", "end", "large", "well", "cross",
    "full", "back", "front", "open", "source", "high", "low",
    # Verbs
    "including", "using", "leveraging", "building", "developing",
    "develop", "designing", "managing", "leading", "working",
    "writing", "understanding", "ensuring", "implementing",
    "optimizing", "collaborating", "maintaining", "creating",
    "delivering", "integrating", "deploying", "supporting",
    "defining", "driving", "enabling", "handling", "processing",
    # Generic nouns
    "proficiency", "familiarity", "knowledge", "ability",
    "tools", "practices", "frameworks", "platforms",
    "systems", "solutions", "services", "concepts", "principles",
    "methodologies", "technologies", "libraries",
    "environments", "applications", "processes", "pipelines",
    "reviews", "reusable", "reliability", "performance",
    # Single generic words that appear in JDs but aren't skills
    "data", "cloud", "code", "design", "ci", "cd",
    "or", "and", "the", "for", "with", "from", "into",
    "years", "year", "months", "month",
    # Connector fragments that slip through splitting
    "and cloud", "and cost", "or gcp", "and monitoring",
    "and performance", "and cost", "efficiency in cloud",
}

# ─────────────────────────────────────────────
#  SECTION HEADERS
#  Used only to filter Layer 2 JD extraction
# ─────────────────────────────────────────────
SECTION_HEADERS = {
    "objective", "summary", "projects", "certifications",
    "publications", "activities", "contact", "interests",
    "references", "profile", "overview", "about",
    "key skills", "key responsibilities",
    "nice to have", "required", "preferred",
}

# ─────────────────────────────────────────────
#  KNOWN REAL SKILLS
#  Connector phrases that look like noise but
#  are actually valid skills from JDs
# ─────────────────────────────────────────────
KNOWN_REAL_SKILLS = {
    "window functions", "query optimization", "performance tuning",
    "data pipeline", "data pipelines", "data modeling", "data quality",
    "data engineering", "data integration", "data warehouse",
    "data lake", "data lakehouse", "data analysis", "data visualization",
    "data science", "data structures", "machine learning",
    "deep learning", "computer vision", "natural language processing",
    "real time", "batch processing", "streaming",
    "ci/cd", "rest api", "object oriented", "unit testing",
    "code review", "system design", "big data",
    "cloud computing", "cloud native",
}

# ─────────────────────────────────────────────
#  JOB TITLE WORDS
#  Used to strip title from name candidates
# ─────────────────────────────────────────────
JOB_TITLE_WORDS = {
    "engineer", "developer", "analyst", "scientist", "manager",
    "lead", "architect", "consultant", "specialist", "director",
    "officer", "intern", "associate", "senior", "junior", "head",
    "vp", "president", "executive", "contact", "profile", "resume",
    "cv", "data", "software", "cloud", "solutions", "technical",
    "ai", "ml", "full", "stack", "backend", "frontend",
}

# ─────────────────────────────────────────────
#  ORG BLACKLIST
#  Words/phrases that spaCy incorrectly tags
#  as ORG entities. Only pure tech tool names
#  and job titles — NOT domain words, since
#  "Healthcare Inc" or "Retail Group" are
#  legitimate company names.
# ─────────────────────────────────────────────
ORG_BLACKLIST = {
    # Pure tech tools — never a company name
    "spark", "python", "java", "sql", "hadoop", "kafka",
    "airflow", "docker", "kubernetes", "git", "linux",
    "tensorflow", "pytorch", "scala", "pyspark", "aws",
    "azure", "gcp", "databricks", "snowflake", "redshift",
    "bigquery", "hive", "hdfs",
    # Job titles — never a company name
    "data engineer", "software engineer", "data scientist",
    "developer", "analyst", "engineer", "manager",
    # Bullet point artefacts that spaCy tags as ORG
    "• mentored", "• built", "• automated", "• leading",
    "• building", "• full",
    # Architecture/methodology terms
    "medallion architecture", "predictive analytics",
    "azure synapse analytics",
}


# ─────────────────────────────────────────────
#  NAME HELPERS
# ─────────────────────────────────────────────
def _normalise_spaced_name(text):
    """
    Collapses spaced-out names like 'M O H A M M E D F A R I D H'
    into 'MOHAMMED FARIDH'.
    Only collapses sequences of 3+ single uppercase letters.
    Uses 3+ threshold to avoid collapsing 'AI' → 'AI' (already fine)
    while correctly collapsing 'M O H A M M E D'.
    """
    # Match 3 or more single uppercase letters separated by spaces
    spaced = re.findall(r'(?:[A-Z] ){2,}[A-Z]', text)
    result = text
    for match in spaced:
        collapsed = match.replace(' ', '')
        result = result.replace(match, collapsed + ' ', 1)
    return result


def _clean_name_line(line):
    """Strips label prefixes, emails, phones, special chars."""
    # Remove label prefixes like "NAME:", "Name :"
    line = re.sub(r'^(?:name\s*[:\-]\s*)', '', line.strip(), flags=re.IGNORECASE)
    # Remove emails
    line = re.sub(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '', line)
    # Remove URLs
    line = re.sub(r'https?://\S+', '', line)
    # Remove phone numbers
    line = re.sub(r'[\+\d\-\(\)]{7,}', ' ', line)
    # Remove special chars except spaces and apostrophes
    line = re.sub(r'[^\w\s\']', ' ', line)
    line = re.sub(r'\s+', ' ', line).strip()
    return line


def _is_valid_name(words):
    """True if word list is a plausible human name."""
    if not (2 <= len(words) <= 3):
        return False
    if not all(w.replace("'", "").isalpha() for w in words):
        return False
    if any(w.lower() in JOB_TITLE_WORDS for w in words):
        return False
    # Reject single-char words unless it's an initial (capitalised)
    for w in words:
        if len(w) == 1 and not w.isupper():
            return False
    return True


# ─────────────────────────────────────────────
#  NAME EXTRACTION
#  Handles:
#  - All-caps: LAKSHAY GOEL → Lakshay Goel
#  - Spaced: M O H A M M E D → Mohammed (3+ letters threshold)
#  - Prefix: NAME: Singam Vivek Kumar → Singam Vivek Kumar
#  - Name+title: Lakshay Goel Data Engineer → Lakshay Goel
#  - Short surname: Gangadhar K → Gangadhar K
#  - spaCy false positive: skips non-person ORG-like entities
# ─────────────────────────────────────────────
def extract_candidate_name(text):
    # Pre-process: collapse spaced-out names (3+ single letters)
    text_proc = _normalise_spaced_name(text)
    lines_proc = text_proc.strip().split('\n')

    # ── Strategy 1: Check first 5 lines directly ──
    # More reliable than spaCy for resume headers
    for line in lines_proc[:5]:
        cleaned = _clean_name_line(line)
        if not cleaned or len(cleaned) < 2:
            continue

        # Normalise ALL-CAPS → Title Case
        if cleaned.isupper() and len(cleaned.split()) <= 4:
            cleaned = cleaned.title()

        words = cleaned.split()

        # Standard 2-3 word name
        if _is_valid_name(words):
            return cleaned

        # 4-word line: try stripping title words from end
        if len(words) == 4:
            # Try last word
            if words[-1].lower() in JOB_TITLE_WORDS:
                candidate = words[:3]
                if _is_valid_name(candidate):
                    return ' '.join(candidate)
            # Try last 2 words
            if words[-2].lower() in JOB_TITLE_WORDS:
                candidate = words[:2]
                if _is_valid_name(candidate):
                    return ' '.join(candidate)

        # "Gangadhar K" — 2 words, second is single capital initial
        if len(words) == 2:
            if (len(words[1]) == 1
                    and words[1].isupper()
                    and words[0].replace("'", "").isalpha()
                    and words[0].lower() not in JOB_TITLE_WORDS
                    and len(words[0]) > 2):
                return words[0].capitalize() + ' ' + words[1]

    # ── Strategy 2: spaCy PERSON entity ──
    # Run on first 300 chars only — name is always near top
    doc = nlp(text_proc[:300])
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            words = ent.text.strip().split()
            # Extra check: spaCy sometimes tags tool names as PERSON
            # Reject if any word looks like a tech term
            if _is_valid_name(words):
                return ' '.join(w.capitalize() for w in words)

    # ── Strategy 3: ALL-CAPS line regex fallback ──
    for line in lines_proc[:8]:
        cleaned = _clean_name_line(line).strip()
        # Match ALL-CAPS 2-3 word name
        if re.match(r'^[A-Z]{2,}(?:\s[A-Z]{2,}){1,2}$', cleaned):
            title_cased = cleaned.title()
            words = title_cased.split()
            if _is_valid_name(words):
                return title_cased

    return "Candidate"


# ─────────────────────────────────────────────
#  EMAIL EXTRACTION
# ─────────────────────────────────────────────
def extract_candidate_email(text):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, text)
    return emails[0] if emails else "Not provided"


# ─────────────────────────────────────────────
#  EDUCATION EXTRACTION
#  Fixed: requires degree + institution in same
#  sentence to avoid matching skills sections.
#  Added regex section fallback for cases where
#  sentence detection fails (Lakshay, Faridh).
# ─────────────────────────────────────────────
def extract_education(text):
    degree_keywords = [
        "bachelor", "master", "phd", "ph.d", "b.tech", "m.tech",
        "mba", "bca", "mca", "b.sc", "m.sc", "b.e", "m.e",
        "degree", "diploma", "graduate", "undergraduate",
        "b.com", "m.com", "msc", "m.s", "b.s", "be", "btech",
        "bachelor of", "master of", "doctor of", "bba",
    ]
    institution_keywords = [
        "university", "college", "institute", "school",
        "institution", "academy", "iit", "nit", "bits", "iim",
    ]
    score_keywords = [
        "cgpa", "gpa", "percentage", "distinction",
        "first class", "second class", "passed with",
    ]

    doc = nlp(text)
    education = []

    for sent in doc.sents:
        sent_lower = sent.text.lower()
        has_degree      = any(kw in sent_lower for kw in degree_keywords)
        has_institution = any(kw in sent_lower for kw in institution_keywords)
        has_score       = any(kw in sent_lower for kw in score_keywords)

        if has_degree and (has_institution or has_score):
            education.append(sent.text.strip())

    # Fallback: find EDUCATION section header and grab text below it
    # This handles resumes where the education block is a list
    # (like Lakshay's) that doesn't form proper sentences
    if not education:
        match = re.search(
            r'\b(?:education|qualification)[s]?\s*[:\-–]?\s*\n+'
            r'((?:.*\n){1,6})',
            text,
            re.IGNORECASE
        )
        if match:
            block = match.group(1).strip()
            # Only accept if block contains a degree or institution keyword
            block_lower = block.lower()
            if (any(kw in block_lower for kw in degree_keywords) or
                    any(kw in block_lower for kw in institution_keywords)):
                education.append(block[:300])

    return " | ".join(education[:3]) if education else "Not found"


# ─────────────────────────────────────────────
#  EXPERIENCE EXTRACTION
#  Fixed:
#  - Bullet point artefacts ("• Mentored") rejected
#  - Architecture terms rejected ("Medallion Architecture")
#  - Single-word short orgs rejected
#  - All-uppercase short terms rejected (AWS, GCP as orgs)
#  - Orgs that start with bullet chars rejected
# ─────────────────────────────────────────────
def extract_experience(text):
    found = []

    # Years of experience — stop at first matching pattern
    year_patterns = [
        r'\d+\+?\s*years?\s*of\s*(?:professional\s*)?experience',
        r'experience\s*of\s*\d+\+?\s*years?',
        r'\d+\+?\s*years?\s*experience',
        r'\d+\+\s*years?',
    ]
    for pattern in year_patterns:
        matches = re.findall(pattern, text.lower())
        if matches:
            found.append(matches[0])
            break

    # Organisation extraction
    doc = nlp(text)
    real_orgs = []
    seen_lower = set()

    for ent in doc.ents:
        if ent.label_ != "ORG":
            continue

        org = ent.text.strip()
        org_lower = org.lower().strip()

        # Skip empty or too short
        if len(org) < 4:
            continue

        # Skip duplicates
        if org_lower in seen_lower:
            continue

        # Skip bullet point artefacts
        if org.startswith('•') or org.startswith('-') or org.startswith('●'):
            continue

        # Skip if in blacklist
        if org_lower in ORG_BLACKLIST:
            continue

        # Skip if any word matches blacklist
        org_words = [w.lower() for w in org.split()]
        if any(w in ORG_BLACKLIST for w in org_words):
            continue

        # Skip if it's all uppercase and short — likely an acronym/tech term
        # Real company acronyms (JPMC, IBM) are fine — but "AWS", "GCP" aren't orgs
        if org.isupper() and len(org) <= 4:
            continue

        # Skip if it contains commas or slashes — likely a tech stack listing
        if ',' in org or '/' in org:
            continue

        # Skip if all lowercase — proper company names are capitalised
        if org == org.lower():
            continue

        # Skip if it's a number or contains mostly digits
        if org.replace(' ', '').isdigit():
            continue

        # Must contain at least one word of 3+ chars
        # (filters out "& Co", "• B", etc.)
        if not any(len(w) >= 3 for w in org.split()):
            continue

        real_orgs.append(org)
        seen_lower.add(org_lower)

    if real_orgs:
        found.append("Organizations: " + ", ".join(real_orgs[:4]))

    return " | ".join(found[:2]) if found else "Not found"


# ─────────────────────────────────────────────
#  SKILL EXTRACTION
#  Layer 1 (PRIMARY): JD-driven — any domain
#  Layer 2 (FALLBACK): SKILLS_DATABASE
#
#  Fixed: added KNOWN_REAL_SKILLS whitelist so
#  multi-word real skills like "window functions",
#  "performance tuning" aren't filtered as noise
# ─────────────────────────────────────────────
def extract_skills(text, jd_text=None):
    text_lower = text.lower()
    found_skills = set()

    # ── Layer 1: JD-driven dynamic extraction ──
    if jd_text:
        jd_lower = jd_text.lower()
        candidates = re.split(r'[,\n•\-\|/\(\)\[\]]', jd_lower)

        for candidate in candidates:
            candidate = candidate.strip()
            candidate = re.sub(r'\s+', ' ', candidate)

            # Whitelist check first — known real skills bypass filters
            if candidate in KNOWN_REAL_SKILLS:
                if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
                    found_skills.add(candidate)
                continue

            # Max 25 chars, max 3 words
            if not (2 <= len(candidate) <= 25):
                continue
            if len(candidate.split()) > 3:
                continue
            # No digits
            if any(ch.isdigit() for ch in candidate):
                continue
            # No colons
            if ':' in candidate:
                continue
            # Not a stopword
            if candidate in STOP_WORDS:
                continue
            # Not a section header
            if candidate in SECTION_HEADERS:
                continue
            # Not a noise word
            if candidate in NOISE_WORDS:
                continue
            # Not all noise/stopwords
            words = candidate.split()
            if all(w in NOISE_WORDS or w in STOP_WORDS for w in words):
                continue
            # At least one word must be 3+ chars (filters "ci", "cd", "or")
            if not any(len(w) >= 3 for w in words):
                continue

            if re.search(r'\b' + re.escape(candidate) + r'\b', text_lower):
                found_skills.add(candidate)

    # ── Layer 2: SKILLS_DATABASE fallback ──
    for skill in SKILLS_DATABASE:
        if skill not in found_skills:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                found_skills.add(skill)

    return list(found_skills)


# ─────────────────────────────────────────────
#  PROCESS RESUME
# ─────────────────────────────────────────────
def process_resume(text, jd_text=None):
    return {
        "name":       extract_candidate_name(text),
        "email":      extract_candidate_email(text),
        "skills":     extract_skills(text, jd_text),
        "education":  extract_education(text),
        "experience": extract_experience(text)
    }


# ─────────────────────────────────────────────
#  PROCESS JD
# ─────────────────────────────────────────────
def process_jd(text):
    return {
        "all_skills":  extract_skills(text, text),
        "education":   extract_education(text),
        "experience":  extract_experience(text)
    }