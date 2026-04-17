# 🔍 HireIQ — AI-Powered Resume Screener

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-ff4b4b?logo=streamlit)](https://hireiq-fpsb54fa7o4pkm8wxljhk8.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python)](https://www.python.org/)
[![spaCy](https://img.shields.io/badge/NLP-spaCy-09a3d5)](https://spacy.io/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff4b4b?logo=streamlit)](https://streamlit.io/)

HireIQ is a fully local, AI-powered resume screening web app. Upload a Job Description and multiple candidate resumes — HireIQ scores, ranks, and explains results using a hybrid 5-dimension scoring engine built on BERT, TF-IDF, and NLP-based skill extraction.

**No external APIs. No internet dependency during scoring. Works for any domain.**

---

## Live Demo

🔗 **[https://hireiq-fpsb54fa7o4pkm8wxljhk8.streamlit.app](https://hireiq-fpsb54fa7o4pkm8wxljhk8.streamlit.app)**

```
Email:    hr@strive4x.com
Password: hr@123
```

---

## Features

- Upload JD as PDF, TXT, or pasted text
- Bulk upload candidate resumes (PDF)
- AI scoring across 5 dimensions with per-candidate score explanations
- Matched and missing skill badges per candidate
- Export results as CSV, Excel, or PDF
- Admin panel for user management — no public signup
- Secure login with bcrypt + OTP-based password reset via Gmail SMTP
- Fully domain-independent — works for any job role out of the box

---

## Scoring System

HireIQ uses a **weighted hybrid model** combining semantic AI, traditional ML, and rule-based NLP:

| Dimension | Weight | Method |
|---|---|---|
| Skill Match | **50%** | Word boundary matching + BERT semantic similarity |
| Semantic (BERT) | **30%** | `all-MiniLM-L6-v2` sentence embeddings |
| Experience | **10%** | Year range extraction from JD and resume text |
| TF-IDF | **5%** | Cosine similarity on TF-IDF vectors |
| Job Title | **5%** | Dynamic keyword match from JD header |

### Skill Matching Priority Chain

Each JD skill is matched against resume skills using this priority chain:

```
1. Exact match after normalisation              → 1.0
2. Plural / singular variation                  → 1.0
3. Substring containment (len > 3)              → 0.9
4. Equivalent alias group (e.g. spark/pyspark)  → 0.85
5. BERT semantic similarity > 0.85              → 0.85
   BERT semantic similarity > 0.70              → 0.70
   BERT semantic similarity > 0.55              → 0.50
6. No match                                     → 0.0
```

**BERT early exit:** BERT is only invoked when two skills share at least one word of 4+ characters, preventing 1200+ unnecessary inference calls per resume.

### Skill Extraction — 3 Layers

| Layer | Source | Method |
|---|---|---|
| Layer 1 (Primary) | JD-driven | Splits JD on delimiters, validates candidates, matches in resume via `\b` |
| Layer 2 (Fallback) | Skills database (~200 skills) | Checks every skill against resume text via `\b` |
| Layer 3 | Short exact skills | Handles `r`, `go`, `c` as exact matches |

> Layer 1 makes HireIQ domain-independent — skills are extracted from the JD itself, not from a hardcoded list.

### Required vs Preferred Skills

`split_jd_sections()` detects preferred/nice-to-have sections and scores them separately:

```
Final Skill Score = (0.85 × required_score) + (0.15 × preferred_score)
```

---

## Architecture

```
hireiq/
├── src/
│   ├── parser.py        ← PDF extraction (3 strategies: word-level, column-aware, fallback)
│   ├── nlp.py           ← Name, email, phone, skills, education, experience extraction
│   ├── matcher.py       ← 5-dimension scoring engine
│   ├── database.py      ← SQLite CRUD
│   ├── auth.py          ← Login, OTP, admin functions
│   └── exporter.py      ← CSV, Excel, PDF export
├── .streamlit/
│   └── config.toml
├── app.py               ← Streamlit UI
├── setup_db.py          ← DB init + default admin account
├── .python-version      ← Pins Python 3.11.9
├── packages.txt         ← System deps (libgomp1 for spaCy/torch)
└── requirements.txt
```

### PDF Parsing — 3 Strategies (tried in order)

1. **Word-level extraction** grouped by vertical position — handles single-column, two-column, and mixed layouts
2. **Column-aware crop** at 48% page width — extracts left/right halves separately and joins them
3. **Standard pdfplumber** `extract_text()` as fallback

### NLP Pipeline

- **Name extraction:** 3-strategy chain — line scan → spaCy PERSON entity → ALL CAPS regex. Handles `NAME: Bharath` format, ALL CAPS names, spaced names like `M O H A M M E D`, and collapsed names like `MOHAMMEDFARIDH`
- **Skill extraction:** JD-driven Layer 1 + database fallback + exact short skill matching
- **Experience:** Regex patterns for `X years of experience`, `X+ years`, `over X years`, etc.
- **Education:** Section header detection + degree/institution keyword matching

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11.9 |
| Frontend | Streamlit |
| NLP | spaCy `en_core_web_sm`, NLTK |
| Semantic AI | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| ML | scikit-learn (TF-IDF, cosine similarity) |
| PDF Parsing | pdfplumber |
| Database | SQLite |
| Security | bcrypt |
| Export | pandas, fpdf2, openpyxl |
| Deployment | Streamlit Cloud |

---

## Local Setup

### Prerequisites
- Python 3.11.9
- CMD terminal on Windows (not PowerShell)

```bash
# Clone
git clone https://github.com/aishnabirla/hireiq.git
cd hireiq

# Virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Init database
python setup_db.py

# Run
streamlit run app.py
```

Open `http://localhost:8501` and login with `hr@strive4x.com` / `hr@123`.

---

## Database Schema

```sql
users            (id, name, email, password_hash, role, created_at)
job_descriptions (id, user_id, title, content, uploaded_at)
resumes          (id, jd_id, candidate_name, candidate_email, file_name, raw_text, uploaded_at)
evaluations      (id, resume_id, jd_id, match_score, matched_skills,
                  missing_skills, education, experience, evaluated_at)
```

---

## Deployment

Deployed on **Streamlit Cloud**. Key configuration:

| File | Purpose |
|---|---|
| `.python-version` | Pins Python `3.11.9` |
| `packages.txt` | Installs `libgomp1` (required by spaCy/torch on Linux) |
| `requirements.txt` | `torch` fetched via PyTorch CPU index to avoid GPU dependency |

Database writes to `/tmp/resume_screener.db` since the Streamlit Cloud root filesystem is read-only.

> ⚠️ `/tmp` is cleared on app restart — data does not persist across reboots on the free tier.

---

## User Flow

```
Login
 └── Step 1: Upload Job Description (PDF / TXT / paste)
 └── Step 2: Bulk upload candidate resumes (PDF)
 └── Step 3: Evaluate → ranked results with score breakdown
              └── Export: CSV / Excel / PDF
              └── Admin Panel (admin role only)
```

---

## Scoring Evolution

| Version | Weights | Peak Score |
|---|---|---|
| V1 | TF-IDF 30% · BERT 50% · Skills 20% | ~45% |
| V2 | TF-IDF 20% · BERT 40% · Skills 40% | ~56% |
| V3 | Added Experience + Title dimensions | ~68% |
| V4 (current) | TF-IDF 5% · BERT 30% · Skills 50% · Exp 10% · Title 5% | **80.41%** |

*Benchmark: Senior Data Engineer profile with 10+ years exp, Spark/Kafka/Databricks/Python.*