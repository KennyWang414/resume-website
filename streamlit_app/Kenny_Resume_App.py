# -*- coding: utf-8 -*-
"""
AN6100 Programming Essential - Assignment Part 1 (dynamic resume)
Name: Wang Gaoyang (Kenny)

Run it with:
    streamlit run Kenny_Resume_App.py

HOW TO UPDATE THIS RESUME
-------------------------
All of the content lives in Section 1 ("RESUME CONTENT") as plain
dictionaries and lists. To add a new project, internship or activity,
copy one of the existing dictionaries, paste it into the same list and
edit the text. The page functions in Section 4 read the lists with
loops, so every page, the job-match tool, the contact form and the
downloadable text resume update by themselves. Nothing else needs to change.

The resume is split into short pages (see PAGES) so each one fits on the
screen; the sidebar directory switches between them.

Two small conventions in the text:
- Wrap a key figure or phrase in double asterisks, e.g. "**$1.5M**", to highlight it.
- The portrait and the company and school logos live in a folder called
  "images" next to this file, using the file names given in PROFILE,
  EXPERIENCE and EDUCATION. If a logo file is missing, an initials badge
  is shown instead, and a missing portrait is simply left out.

Constraints followed: no JavaScript, no class, no lambda, no pandas.
"""

import os
import base64
import streamlit as st

# Folder that holds the portrait and logo images (next to this .py file)
IMAGE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")


# =====================================================================
# 1. RESUME CONTENT  (edit this section to update the resume)
# =====================================================================

PROFILE = {
    "name": "Wang Gaoyang, Kenny",
    "short_name": "Kenny Wang",
    "symbol": "Kw",
    "tile_top_left": "MSBA",
    "tile_top_right": "2027",
    "tile_caption": "Chemistry + Analytics",
    "tagline": "Business analytics student at NTU Singapore",
    "photo": "portrait.jpg",
    "intro": [
        "Stepping from chemistry into business analytics may seem like a drastic shift, but for me, the core "
        "objective remains unchanged: ==using data to solve complex problems==. My coursework has refined my "
        "analytical toolkit in Python, SQL, and R, while my professional experiences in strategic advisory and "
        "the ESG industry have offered me hands-on client exposure. From predicting material properties to "
        "advising clients across **$1.5M** in strategic mandates, I leverage my analytics toolkit to drive "
        "decision-making, turning complex information into insights that people can act on.",
        "As an analyst, I always think about what the data truly means for the client; as a leader, I focus on "
        "fostering a collaborative environment; as a job-seeker, I am looking for a role that can translate "
        "rigorous technical analysis into strategic client value.",
    ],
    "facts": [
        ["Studying", "MSc Business Analytics, Nanyang Business School (2026–2027)", "🎓"],
        ["Background", "BSc in Chemistry, Minor in Business, HKUST", "⚗️"],
        ["Available", "Part-time internship Jan–Feb 2027, full-time internship Mar–Dec 2027", "📅"],
        ["Languages", "English (IELTS **7.5**), Mandarin and Cantonese (native)", "🗣️"],
    ],
    "status": "Open to analyst internships from Jan 2027",
    "linkedin": "https://www.linkedin.com/in/kenny-wang-7966ba286",
    "email": "WANG2537@e.ntu.edu.sg",
    "last_updated": "September 2026",
}

# Numbers that count up when the page loads
HIGHLIGHTS = [
    {"value": 7, "suffix": "", "label": "advisory mandates supported, about $1.5M in contract value"},
    {"value": 32, "suffix": "%", "label": "projected cut in a sports centre's annual carbon emissions"},
    {"value": 12, "suffix": "", "label": "buildings covered by my carbon and energy audit reports"},
    {"value": 3, "suffix": "", "label": "languages: English, Mandarin and Cantonese"},
]

# Pages in the sidebar directory: [page key, two-letter symbol, label]
PAGES = [
    ["about", "Ab", "About me"],
    ["skills", "Sk", "Skills & Education"],
    ["work", "Ex", "Experience & Projects"],
    ["leadership", "Ld", "Leadership & Beyond"],
    ["job-match", "Jm", "Job Match"],
    ["contact", "Ct", "Contact me"],
]

# Choices in the contact form: [what the visitor sees, the email subject line it creates]
CONTACT_PURPOSES = [
    ["A job or internship opening", "Internship or job opportunity for Kenny Wang"],
    ["Collaborating on a project", "Project collaboration with Kenny Wang"],
    ["Something else", "Hello from your online resume"],
]

# Emoji shown next to each page and section title
ICONS = {"skills": "🧪", "education": "🎓", "experience": "💼", "projects": "📊", "leadership": "🌟",
         "beyond": "🏀", "job-match": "🎯", "contact": "✉️"}

# Colour names map to CSS variables defined in the style sheet (Section 2)
SKILL_GROUPS = [
    {
        "title": "Programming & Analytics",
        "colour": "copper",
        "skills": [
            ["Py", "Python", "pandas, NumPy, scikit-learn, RDKit"],
            ["R", "R", "ggplot2, regression models"],
            ["C", "C", "Programming fundamentals"],
            ["Kn", "KNIME", "Visual data workflows"],
            ["Xl", "Excel", "Pivot tables, XLMiner"],
        ],
    },
    {
        "title": "Querying & Data Visualization",
        "colour": "sodium",
        "skills": [
            ["Sq", "SQL", "MySQL queries and joins"],
            ["Ns", "NoSQL", "MongoDB document databases"],
            ["Tb", "Tableau", "Dashboards and visual stories"],
        ],
    },
    {
        "title": "Languages",
        "colour": "lithium",
        "skills": [
            ["En", "English", "Business level, IELTS 7.5"],
            ["Ma", "Mandarin", "Native"],
            ["Ca", "Cantonese", "Native"],
        ],
    },
]

EXPERIENCE = [
    {
        "role": "Strategic Consultant Intern",
        "company": "Cushman & Wakefield",
        "place": "China",
        "dates": "Jul – Aug 2025",
        "logo": "cushman_wakefield.png",
        "initials": "C&W",
        "points": [
            "Researched Chengdu's apartment and office market, analysing supply and demand, rental rates "
            "and absorption trends for a client weighing an investment in a mixed-use building.",
            "Prepared client pitch materials with senior consultants for **7 advisory mandates**, which together "
            "secured about **$1.5M** in contract value.",
        ],
    },
    {
        "role": "ESG Projects Intern",
        "company": "CMA Testing Limited",
        "place": "Hong Kong",
        "dates": "May – Aug 2024",
        "logo": "cma_testing.png",
        "initials": "CMA",
        "points": [
            "Drafted Carbon Audit Reports for **7 LCSD buildings** and helped complete Energy Audit Reports for "
            "**5 commercial buildings**, following ISO standards and Cap. 610.",
            "Led a project to improve a local sports centre's sustainability, recommending IoT lighting, "
            "cooling coatings and carbon purifiers, projected to cut annual carbon emissions by **32%**.",
        ],
    },
]

PROJECTS = [
    {
        "title": "DBS: purpose-driven transformation",
        "dates": "Aug – Sep 2026",
        "meta": "NTU, team of 5",
        "colour": "copper",
        "tools": ["Benchmarking", "Regression", "Impact measurement"],
        "points": [
            "Evaluated **15 years** of DBS's digital and ESG transformation, and tested the bank's own solutions statistically.",
            "Responsible for the sustainability workstream: emissions disclosure across **9** priority sectors, and "
            "employee engagement against Asia Pacific peers.",
            "Proposed a statistical approach to measure the real social impact of DBS's projects.",
        ],
    },
    {
        "title": "Predicting polymer glass transition temperature",
        "dates": "Feb – May 2025",
        "meta": "HKUST, team of 4",
        "colour": "potassium",
        "tools": ["Python", "RDKit", "Random forest"],
        "points": [
            "Engineered molecular descriptors from monomer SMILES strings with RDKit and trained a random forest regression model.",
            "Led feature selection and cross-validation, offering a faster alternative to lab measurement for early material screening.",
        ],
    },
    {
        "title": "Predicting bank marketing response",
        "dates": "Feb – May 2024",
        "meta": "HKUST, course project",
        "colour": "sodium",
        "tools": ["XLMiner", "Classification tree", "k-NN", "Neural network"],
        "points": [
            "Compared classification tree, k-NN and neural network models to predict which customers would take up a banking product.",
            "Selected the neural network on accuracy and documented the method in a **13-page** report.",
        ],
    },
]

EDUCATION = [
    {
        "years": "2026 – 2027",
        "note": "Expected Dec 2027",
        "degree": "MSc in Business Analytics",
        "logo": "ntu.png",
        "initials": "NTU",
        "school": "Nanyang Business School, Nanyang Technological University, Singapore",
        "coursework": "Data Management and Visualisation, Analytics Strategy",
    },
    {
        "years": "2021 – 2025",
        "note": "Sep 2021 – Jul 2025",
        "degree": "BSc in Chemistry, Minor in Business",
        "logo": "hkust.png",
        "initials": "HKUST",
        "school": "Hong Kong University of Science and Technology (HKUST)",
        "coursework": "Statistical Machine Learning Methods for Chemical Data Analysis, Exploring and "
                      "Visualizing Data, Intermediate Investments, Operations Management",
    },
    {
        "years": "Summer 2024",
        "note": "Jun – Jul 2024",
        "degree": "Summer exchange",
        "logo": "korea_university.png",
        "initials": "KU",
        "school": "Korea University, Seoul",
        "coursework": "Managerial Accounting",
    },
]

LEADERSHIP = [
    {
        "title": "Future Banking Bridging Programme, HKIB",
        "role": "Participant, Nov – Dec 2025",
        "emoji": "🏦",
        "colour": "sodium",
        "points": [
            "Worked with **6** students from other universities and presented to senior bankers and around **100** "
            "attendees on using soft skills to improve customer service in banking.",
            "Our team placed **4th out of 8**.",
        ],
    },
    {
        "title": "Generative AI Hackathon for the Sustainable Development Goals",
        "role": "Team lead, Sep – Oct 2024",
        "emoji": "🤖",
        "colour": "potassium",
        "points": [
            "Led **5** HKUST first-year students to research employment outcomes for LGBTQIA+ jobseekers.",
            "Built an AI-assisted job search site on WIX and POE based on what we found.",
        ],
    },
    {
        "title": "Counselling Prefect, WTSMC",
        "role": "President, Sep 2018 – Sep 2019",
        "emoji": "🤝",
        "colour": "copper",
        "points": [
            "Assigned duties across **10** executive committee members according to their strengths.",
            "Organised self-development activities for **30** members and **over a hundred** new students.",
        ],
    },
]

# Beyond work: [title, text, emoji, colour, short tag]
INTERESTS = [
    ["Volunteering",
     "At the Ebenezer School & Home for the Visually Impaired in Hong Kong, I guided students with special "
     "educational needs as they assembled simple motor fans and played checkpoint games.",
     "💛", "lithium", "Ebenezer School & Home, Hong Kong"],
    ["Basketball",
     "Years of competitive play for my high school and community centre teams built my teamwork, "
     "discipline and resilience.",
     "🏀", "sodium", "High school and community centre teams"],
]

# Job-match tool: keywords to look for in a job description, and my evidence for each skill
MATCH_RULES = [
    {"skill": "SQL & databases",
     "keywords": ["sql", "mysql", "database", "databases", "query", "queries", "nosql", "mongodb"],
     "evidence": "Writes MySQL and MongoDB queries in MSBA Data Management and Visualisation."},
    {"skill": "Python",
     "keywords": ["python", "pandas", "numpy", "scikit"],
     "evidence": "Built a random forest regression model in Python with RDKit (polymer project)."},
    {"skill": "Dashboards & visualisation",
     "keywords": ["tableau", "dashboard", "dashboards", "visualisation", "visualization", "visualise",
                  "visualize", "charts", "reporting"],
     "evidence": "Tableau and ggplot2; visualisation coursework at both HKUST and NTU."},
    {"skill": "Excel",
     "keywords": ["excel", "spreadsheet", "spreadsheets", "pivot"],
     "evidence": "Pivot tables, and three classification models built in XLMiner (bank marketing project)."},
    {"skill": "Statistics & modelling",
     "keywords": ["statistics", "statistical", "regression", "machine learning", "model", "models",
                  "modelling", "modeling", "predictive", "forecast", "forecasting", "classification"],
     "evidence": "Random forest, classification tree, k-NN and neural network models; statistical evaluation in the DBS case."},
    {"skill": "Market & customer insight",
     "keywords": ["market", "customer", "customers", "consumer", "consumers", "insight", "insights",
                  "research", "trends", "sales"],
     "evidence": "Chengdu property market research at Cushman & Wakefield; bank customer response modelling."},
    {"skill": "Stakeholder communication",
     "keywords": ["stakeholder", "stakeholders", "present", "presentation", "presentations", "communicate",
                  "communication", "client", "clients", "storytelling"],
     "evidence": "Pitch materials for 7 advisory mandates; presented to senior bankers at the HKIB programme."},
    {"skill": "Teamwork & leadership",
     "keywords": ["team", "teams", "teamwork", "collaborate", "collaboration", "cross functional", "lead"],
     "evidence": "Led a 5-person hackathon team; president of a 10-member prefect committee."},
    {"skill": "Chinese languages",
     "keywords": ["mandarin", "chinese", "cantonese", "bilingual"],
     "evidence": "Native Mandarin and Cantonese, plus business-level English."},
]

# Skills I do not have yet: shown honestly as things I would pick up on the job
LEARNING_RULES = [
    {"skill": "Power BI", "keywords": ["power bi", "powerbi"]},
    {"skill": "Google Analytics", "keywords": ["google analytics"]},
    {"skill": "A/B testing", "keywords": ["ab testing", "ab test", "ab tests"]},
    {"skill": "Looker", "keywords": ["looker"]},
    {"skill": "Big data tools", "keywords": ["spark", "hadoop", "big data"]},
    {"skill": "E-commerce domain", "keywords": ["ecommerce", "e commerce", "online retail"]},
]

SAMPLE_JOB = (
    "Data Analyst Intern, E-commerce. You will write SQL queries to pull customer and sales data, "
    "build dashboards in Tableau or Power BI, run A/B tests on the checkout flow, and use Python "
    "or Excel to find trends. You will present insights to stakeholders and work closely with the "
    "marketing team. Mandarin is a plus."
)


# =====================================================================
# 2. STYLE SHEET  (colours, fonts and animations; CSS only, no JavaScript)
# =====================================================================

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,800&family=Figtree:ital,wght@0,400;0,600;0,700;1,400&display=swap');

:root {
  --bench: #F5F7F6; --paper: #FFFFFF; --ink: #17242F; --muted: #5A6A76; --rule: #D5DDE1;
  --copper: #0F7C74; --sodium: #B97E08; --lithium: #B8324A; --potassium: #7A5FB5;
  --display: "Bricolage Grotesque", "Avenir Next", "Segoe UI", Helvetica, Arial, sans-serif;
  --body: "Figtree", "Segoe UI", Helvetica, Arial, sans-serif;
}
@property --num { syntax: "<integer>"; initial-value: 0; inherits: false; }

/* ---------- Page frame: compact, so each page fits on the screen ---------- */
.stApp { background: var(--bench); color: var(--ink); font-family: var(--body); }
[data-testid="stMarkdownContainer"], [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span, [data-testid="stMarkdownContainer"] div, .stApp label, .stApp button { font-family: var(--body); }
[data-testid="stHeader"] { background: transparent; height: 2.5rem; }
[data-testid="stExpandSidebarButton"], [data-testid="stSidebarCollapsedControl"] button {
  background: var(--ink) !important; border-radius: 6px !important; }
[data-testid="stExpandSidebarButton"] *, [data-testid="stSidebarCollapsedControl"] button * { color: #FFFFFF !important; }
[data-testid="stMainBlockContainer"], .block-container { max-width: 1160px; padding-top: 2.2rem; padding-bottom: 2rem; }
[data-testid="stMainBlockContainer"] [data-testid="stVerticalBlock"] { gap: 0.9rem; }
footer { visibility: hidden; }
.stMarkdown p, .stMarkdown li { font-size: 1rem; line-height: 1.55; }
.stApp h2.ptitle { font-family: var(--display); font-weight: 800; letter-spacing: -0.01em; color: var(--ink); font-size: 1.9rem;
  padding: 0; margin: 0; line-height: 1.2; }
.stApp h3.part { font-family: var(--display); font-weight: 800; font-size: 1.3rem; color: var(--ink); padding: 0; margin: 0.9rem 0 0.1rem; }
.ico { display: inline-grid; place-items: center; width: 1.7em; height: 1.7em; margin-right: 0.45rem; border-radius: 10px;
  background: #E3F1EE; font-size: 0.72em; vertical-align: 0.12em; }
[data-testid="stHeaderActionElements"] { display: none; }
.stApp .sub { color: var(--muted); margin: 0.35rem 0 0.3rem; font-size: 1rem; }
.intro .mark { font-weight: 700; background: linear-gradient(transparent 55%, #BFE7DF 55%); padding: 0 2px; }
.reveal { animation: rise 0.45s ease-out both; }

/* ---------- Sidebar ---------- */
[data-testid="stSidebar"] { background: var(--ink); }
[data-testid="stSidebar"] * { color: #E8EEF1; }
[data-testid="stSidebarUserContent"] { padding-top: 0.5rem; }
[data-testid="stSidebar"] [data-testid="stVerticalBlock"] { gap: 0.45rem; }
.tile { width: 132px; aspect-ratio: 4 / 5; border: 5px solid var(--copper); border-radius: 6px;
  background: #0E1820; padding: 0.6rem 0.7rem; display: flex; flex-direction: column;
  animation: flame 10s linear infinite; margin: 0.2rem 0 0.5rem; }
@keyframes flame { 0%, 100% { border-color: var(--copper); } 25% { border-color: var(--lithium); }
  50% { border-color: var(--sodium); } 75% { border-color: var(--potassium); } }
.tile .row { display: flex; justify-content: space-between; font-size: 0.72rem; opacity: 0.8; }
.tile .sym { font-family: var(--display); font-weight: 800; font-size: 3.7rem; line-height: 1; margin: auto 0; letter-spacing: -0.03em; }
.tile .nm { font-family: var(--display); font-weight: 600; font-size: 0.9rem; }
.tile .cap { font-size: 0.66rem; opacity: 0.75; white-space: nowrap; }
.stApp .side-name { font-family: var(--display); font-size: 1.2rem; font-weight: 800; margin: 0; }
.side-tag { font-size: 0.86rem; opacity: 0.75; margin: 0.1rem 0 0.5rem; }
.status { display: flex; align-items: center; gap: 0.5rem; font-size: 0.82rem; margin: 0 0 0.4rem; }
.status i { width: 9px; height: 9px; border-radius: 50%; background: #3DDC97; display: inline-block; flex: none;
  animation: pulse 2s ease-out infinite; }
@keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(61, 220, 151, 0.6); } 100% { box-shadow: 0 0 0 9px rgba(61, 220, 151, 0); } }
.dir-title { font-size: 0.78rem; letter-spacing: 0.06em; text-transform: uppercase; opacity: 0.6; margin: 1.1rem 0 0.5rem; }
/* Directory buttons: a bar per page, the current page in green */
[data-testid="stSidebar"] .stButton button { justify-content: flex-start; padding: 0.45rem 0.8rem; min-height: 0; }
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"] { background: transparent; border: 1px solid #3A4B58; }
[data-testid="stSidebar"] [data-testid="stBaseButton-secondary"]:hover { border-color: #FFFFFF; background: rgba(255, 255, 255, 0.06); }
[data-testid="stSidebar"] [data-testid="stBaseButton-primary"] { background: var(--copper); border: 1px solid var(--copper); }
[data-testid="stSidebar"] .stButton button p { font-size: 0.95rem; }
[data-testid="stSidebar"] .stButton button > div, [data-testid="stSidebar"] .stButton button [data-testid="stMarkdownContainer"] {
  justify-content: flex-start; width: 100%; text-align: left; }
[data-testid="stSidebar"] .stDownloadButton button, [data-testid="stSidebar"] [data-testid="stDownloadButton"] button {
  background: transparent; border: 1px dashed #5D7282; width: 100%; }
.updated { font-size: 0.72rem; opacity: 0.55; margin-top: 0.4rem; }

/* ---------- About ---------- */
.hero-grid { display: grid; grid-template-columns: 210px minmax(0, 1fr); gap: 2rem; align-items: start; }
.portrait { width: 100%; aspect-ratio: 4 / 5; object-fit: cover; border-radius: 10px; border: 5px solid var(--copper);
  animation: flame 10s linear infinite; box-shadow: 0 16px 34px rgba(23, 36, 47, 0.16); display: block; }
.stApp .hero-name { font-family: var(--display); font-weight: 800; font-size: clamp(2.1rem, 3.4vw, 3rem);
  line-height: 1.05; letter-spacing: -0.02em; margin: 0; color: var(--ink); }
.stApp .hero-tag { font-family: var(--display); font-size: 1.2rem; color: var(--muted); margin: 0.3rem 0 0.7rem; }
.stApp .intro p { font-size: 1.02rem; margin-bottom: 0.55rem; }
.facts { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin: 0.6rem 0 0; }
.facts > div { background: var(--paper); border: 1px solid var(--rule); border-radius: 6px; padding: 0.45rem 0.7rem; font-size: 0.92rem;
  display: grid; grid-template-columns: 1.8rem 1fr; column-gap: 0.35rem; align-items: center; }
.facts .e { grid-row: 1 / span 2; font-size: 1.2rem; }
.facts .k { color: var(--muted); font-size: 0.78rem; }
.stats { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; margin-top: 0.4rem; }
.stat { background: var(--paper); border: 1px solid var(--rule); border-radius: 6px; padding: 0.7rem 0.9rem; }
.stat .num { font-family: var(--display); font-weight: 800; font-size: 2.1rem; line-height: 1; color: var(--copper);
  counter-reset: num var(--num); animation: count 2.2s ease-out forwards; }
.stat .num::after { content: counter(num) var(--suffix); }
@keyframes count { to { --num: var(--target); } }
.stat .lbl { font-size: 0.82rem; color: var(--muted); margin-top: 0.3rem; line-height: 1.35; }

/* ---------- Periodic table of skills: one row per family ---------- */
.ptable { display: grid; gap: 8px; }
.prow { display: grid; grid-template-columns: 130px repeat(5, minmax(0, 1fr)); gap: 8px; }
.prow .gl { font-weight: 700; font-size: 0.9rem; color: var(--g); border-left: 4px solid var(--g); padding-left: 0.55rem;
  align-self: center; line-height: 1.3; }
.el { background: var(--paper); border: 1px solid var(--rule); border-top: 4px solid var(--g); border-radius: 4px;
  padding: 0.35rem 0.55rem 0.45rem; display: grid; grid-template-columns: auto 1fr; column-gap: 0.5rem; align-items: center;
  transition: transform 0.2s, box-shadow 0.2s; }
.el:hover { transform: translateY(-2px); box-shadow: 0 6px 14px rgba(23, 36, 47, 0.1); }
.el .s { grid-row: 1 / span 2; font-family: var(--display); font-weight: 800; font-size: 1.65rem; line-height: 1; color: var(--g); }
.el .n { font-weight: 700; font-size: 0.9rem; line-height: 1.2; }
.el .d { font-size: 0.74rem; color: var(--muted); line-height: 1.25; }

/* ---------- Logos ---------- */
.logo { flex: none; display: block; border-radius: 7px; box-sizing: border-box; }
.logo.fill { width: 92px; height: 62px; object-fit: cover; }
.logo.box { width: 92px; height: 62px; object-fit: contain; background: #FFFFFF; border: 1px solid var(--rule); padding: 4px; }
.badge { display: grid; place-items: center; font-family: var(--display); font-weight: 800; font-size: 0.85rem;
  color: var(--ink); background: #FFFFFF; border: 1px solid var(--rule); }
.figure { font-family: var(--display); font-weight: 800; color: var(--copper); }

/* ---------- Education (compact rows) ---------- */
.edus { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
.edu { background: var(--paper); border: 1px solid var(--rule); border-radius: 8px; padding: 0.7rem 0.85rem; }
.edu-head { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 0.4rem; }
.edu .yr { font-size: 0.8rem; font-weight: 700; color: var(--copper); margin: 0; }
.edu h4 { font-family: var(--display); font-size: 1.02rem; margin: 0; color: var(--ink); padding: 0; line-height: 1.25; }
.edu .detail { color: var(--muted); margin: 0.15rem 0 0; font-size: 0.86rem; line-height: 1.4; }

/* ---------- Experience cards (side by side) ---------- */
.jobs { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.job { background: var(--paper); border: 1px solid var(--rule); border-radius: 8px; padding: 0.85rem 1rem; }
.job-head { display: flex; align-items: center; gap: 0.85rem; margin-bottom: 0.45rem; }
.job h4 { font-family: var(--display); font-size: 1.08rem; margin: 0; padding: 0; color: var(--ink); }
.stApp .job .org { color: var(--muted); margin: 0; font-size: 0.88rem; }
.stApp .job ul, .stApp .card ul { margin: 0.3rem 0 0; padding-left: 1.1rem; }
.stApp .job li, .stApp .card li { font-size: 0.92rem; margin: 0 0 0.3rem 0; }

/* ---------- Project cards ---------- */
.cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; align-items: stretch; }
.card { background: var(--paper); border: 1px solid var(--rule); border-top: 5px solid var(--g); border-radius: 6px;
  padding: 0.8rem 0.95rem; display: flex; flex-direction: column; }
.stApp .card .when { font-size: 0.8rem; font-weight: 700; color: var(--g); margin: 0; }
.card h4 { font-family: var(--display); font-size: 1.02rem; margin: 0.2rem 0 0; color: var(--ink); padding: 0; }
.stApp .card .meta { color: var(--muted); font-size: 0.84rem; margin: 0.1rem 0 0; padding-bottom: 0.45rem; border-bottom: 1px solid var(--rule); }
.card li::marker { color: var(--g); }
.chips { display: flex; flex-wrap: wrap; gap: 0.3rem; margin-top: auto; padding-top: 0.6rem; }
.chip { font-size: 0.74rem; font-weight: 600; color: var(--g); border: 1px solid var(--g); border-radius: 999px; padding: 0 0.55rem; }

/* ---------- Colourful cards: leadership and beyond work ---------- */
.ccards { display: grid; gap: 12px; }
.ccards.three { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.ccards.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.ccard { background: var(--paper); border: 1px solid var(--rule); border-radius: 10px; padding: 0.85rem 1rem 0.8rem;
  position: relative; overflow: hidden; }
.ccard::before { content: ""; position: absolute; inset: 0 0 auto 0; height: 5px; background: var(--g); }
.ccard .top { display: flex; gap: 0.7rem; align-items: center; margin-bottom: 0.45rem; }
.ccard .emoji { width: 44px; height: 44px; border-radius: 12px; display: grid; place-items: center; font-size: 1.45rem; flex: none;
  background: color-mix(in srgb, var(--g) 14%, white); }
.ccard h4 { font-family: var(--display); font-size: 1rem; line-height: 1.25; margin: 0; padding: 0; color: var(--ink); }
.pill { display: inline-block; font-size: 0.74rem; font-weight: 700; color: var(--g); border-radius: 999px; padding: 0.05rem 0.55rem;
  margin-top: 0.2rem; background: color-mix(in srgb, var(--g) 12%, white); }
.stApp .ccard ul { margin: 0.2rem 0 0; padding-left: 1.1rem; }
.stApp .ccard li { font-size: 0.92rem; margin: 0 0 0.3rem; }
.stApp .ccard p { font-size: 0.92rem; margin: 0; }
.ccard li::marker { color: var(--g); }
.ccard .figure { color: var(--g); }

/* ---------- Job match ---------- */
.stApp .score { font-family: var(--display); font-weight: 800; font-size: 3rem; color: var(--copper); line-height: 1; margin: 0; }
.ev { background: var(--paper); border: 1px solid var(--rule); border-left: 5px solid var(--copper); border-radius: 4px; padding: 0.5rem 0.8rem; }
.ev b { display: block; }
.ev span { font-size: 0.88rem; color: var(--muted); }
.evs { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px; margin-bottom: 0.8rem; }
.ev-title { font-weight: 700; margin: 0 0 0.4rem; }
.gaps { display: flex; flex-wrap: wrap; gap: 0.45rem; }
.gaps span { border: 1px solid var(--sodium); color: var(--sodium); font-weight: 700; font-size: 0.86rem;
  border-radius: 999px; padding: 0.1rem 0.7rem; background: var(--paper); }
.bar { height: 10px; background: var(--rule); border-radius: 999px; overflow: hidden; margin-top: 0.7rem; }
.bar span { display: block; height: 100%; background: var(--copper); border-radius: 999px; animation: grow 1.4s ease-out both; }
@keyframes grow { from { width: 0; } }

/* ---------- Contact page: the reaction plays when the page opens ---------- */
.st-key-reaction { background: var(--ink); border-radius: 10px; padding: 1.2rem 1.2rem 1rem; }
.finale { color: #FFFFFF; text-align: center; }
.stApp .finale p { color: #C9D4DB; margin: 0; }
.eq { display: flex; align-items: center; justify-content: center; gap: clamp(0.6rem, 2vw, 1.4rem); flex-wrap: wrap; margin: 0.8rem 0 0.6rem; }
.rx { width: 92px; aspect-ratio: 4 / 5; border-radius: 6px; border: 4px solid var(--c); background: #0E1820;
  display: flex; flex-direction: column; justify-content: center; }
.rx .rs { font-family: var(--display); font-weight: 800; font-size: 2.4rem; line-height: 1; color: #FFFFFF; }
.rx .rn { font-size: 0.78rem; color: #C9D4DB; margin-top: 0.25rem; }
.finale .op { font-family: var(--display); font-weight: 800; font-size: 2rem; color: #C9D4DB; }
.arrow { display: block; width: clamp(50px, 7vw, 100px); height: 4px; background: #C9D4DB; position: relative; transform-origin: left center; }
.arrow::after { content: ""; position: absolute; right: -2px; top: -7px; border-left: 14px solid #C9D4DB;
  border-top: 9px solid transparent; border-bottom: 9px solid transparent; }
.sparks { display: flex; justify-content: center; flex-wrap: wrap; gap: 7px; margin: 0.2rem 0 0.2rem; }
.finale .spark { width: 36px; height: 36px; border: 1px solid #5D7282; border-radius: 4px; display: grid; place-items: center;
  font-family: var(--display); font-weight: 800; font-size: 0.85rem; color: #FFFFFF; }
.from-left { animation: in-left 0.9s ease-out both; }
.from-right { animation: in-right 0.9s ease-out both; }
.pop { animation: pop 0.45s ease-out 0.8s both; }
.draw { animation: draw 0.5s ease-out 1s both; }
.product { animation: pop 0.6s ease-out 1.3s both, glow 3s ease-in-out 2s infinite; }
.finale .spark { animation: fly 1s ease-out both; }
@keyframes rise { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }
@keyframes in-left { from { opacity: 0; transform: translateX(-40vw) rotate(-40deg); } to { opacity: 1; transform: none; } }
@keyframes in-right { from { opacity: 0; transform: translateX(40vw) rotate(40deg); } to { opacity: 1; transform: none; } }
@keyframes pop { from { opacity: 0; transform: scale(0.2); } to { opacity: 1; transform: none; } }
@keyframes draw { from { transform: scaleX(0); } to { transform: scaleX(1); } }
@keyframes fly { from { opacity: 0; transform: translate(var(--x), var(--y)) rotate(var(--r)); } to { opacity: 1; transform: none; } }
@keyframes glow { 0%, 100% { box-shadow: 0 0 0 0 rgba(15, 124, 116, 0); } 50% { box-shadow: 0 0 30px 6px rgba(15, 124, 116, 0.65); } }

/* Contact form (a plain HTML form, like the static page) and LinkedIn card */
.mailform { background: var(--paper); border: 1px solid var(--rule); border-radius: 10px; padding: 1rem 1.1rem; display: grid; gap: 0.6rem; }
.mailform label { display: grid; gap: 0.25rem; font-size: 0.88rem; font-weight: 700; color: var(--ink); }
.mailform select, .mailform textarea { font: inherit; font-size: 0.95rem; font-weight: 400; color: var(--ink); background: var(--bench);
  border: 1px solid var(--rule); border-radius: 6px; padding: 0.5rem 0.65rem; width: 100%; box-sizing: border-box; }
.mailform textarea { resize: vertical; min-height: 8.5rem; }
.mailform button { font: inherit; font-weight: 700; font-size: 1rem; color: #FFFFFF; background: var(--copper); border: 0;
  border-radius: 6px; padding: 0.6rem 1.2rem; cursor: pointer; justify-self: start; }
.mailform button:hover { background: #0B5F59; }
.stApp .mailform .tip { color: var(--muted); font-size: 0.82rem; margin: -0.2rem 0 0; }
.linkedin { background: var(--ink); color: #FFFFFF; border-radius: 10px; padding: 1.2rem 1.2rem; display: flex; flex-direction: column; gap: 0.6rem; }
.stApp .linkedin h3 { font-family: var(--display); font-size: 1.3rem; font-weight: 800; color: #FFFFFF; margin: 0; padding: 0; }
.stApp .linkedin p { color: #C9D4DB; font-size: 0.95rem; margin: 0; }
.linkedin .li-btn { display: flex; align-items: center; justify-content: center; gap: 0.6rem; background: #0A66C2; color: #FFFFFF !important;
  text-decoration: none; font-weight: 700; font-size: 1.05rem; padding: 0.75rem 1rem; border-radius: 8px; margin-top: 0.4rem; }
.linkedin .li-btn:hover { background: #084F97; }
.linkedin .li-badge { background: #FFFFFF; color: #0A66C2; font-weight: 800; font-family: Arial, sans-serif; border-radius: 4px;
  padding: 0 0.3rem; font-size: 0.95rem; line-height: 1.35; }

/* Job match: make the paste box obvious */
.st-key-jdbox [data-testid="stTextAreaRootElement"], .st-key-jdbox .stTextArea [data-baseweb="textarea"] { border: 2px dashed var(--copper) !important; }
.st-key-jdbox [data-testid="stWidgetLabel"] p { font-weight: 700; font-size: 1rem; }

/* ---------- Streamlit widgets: fixed colours so they look right in light AND dark mode ---------- */
[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p { color: var(--ink) !important; }
[data-testid="stExpander"] details { background: var(--paper) !important; border: 1px solid var(--rule) !important; border-radius: 6px !important; }
[data-testid="stExpander"] summary { background: var(--paper) !important; border-radius: 6px; }
[data-testid="stExpander"] summary:hover, [data-testid="stExpander"] details[open] summary { background: #EEF3F2 !important; }
[data-testid="stExpander"] summary *, [data-testid="stExpanderDetails"] * { color: var(--ink) !important; }
[data-testid="stExpanderDetails"] .figure { color: var(--copper) !important; }
[data-testid="stTextAreaRootElement"], .stTextArea [data-baseweb="textarea"],
[data-testid="stTextInputRootElement"], .stTextInput [data-baseweb="input"] { background: var(--paper) !important; border: 1px solid var(--rule) !important; }
[data-testid="stTextAreaRootElement"] textarea, .stTextArea textarea, .stTextInput input { color: var(--ink) !important; background: var(--paper) !important; }
[data-testid="stSelectbox"] div[role="combobox"], .stSelectbox [data-baseweb="select"] > div { background: var(--paper) !important; border-color: var(--rule) !important; color: var(--ink) !important; }

/* Main-area buttons */
[data-testid="stMain"] [data-testid="stBaseButton-primary"] { background: var(--copper); border: 1px solid var(--copper); color: #FFFFFF; font-weight: 700; }
[data-testid="stMain"] [data-testid="stBaseButton-primary"]:hover { background: #0B5F59; }
[data-testid="stMain"] [data-testid="stBaseButton-primary"] * { color: #FFFFFF !important; }
[data-testid="stMain"] [data-testid="stBaseButton-secondary"] { background: var(--paper); border: 1px solid var(--rule); color: var(--ink); }
[data-testid="stMain"] [data-testid="stBaseButton-secondary"] * { color: var(--ink) !important; }
[data-testid="stMain"] [data-testid*="FormSubmit"] { background: var(--copper); border: 1px solid var(--copper); }
[data-testid="stMain"] [data-testid*="FormSubmit"] * { color: #FFFFFF !important; font-weight: 700; }

/* Small screens */
@media (max-width: 900px) {
  .stats, .facts { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .cards, .ccards.three, .ccards.two, .evs, .jobs, .edus { grid-template-columns: 1fr; }
  .prow { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .prow .gl { grid-column: 1 / -1; }
  .hero-grid { grid-template-columns: 1fr; }
  .hero-grid .photo-col { max-width: 240px; }
}
@media (prefers-reduced-motion: reduce) {
  .tile, .portrait, .status i, .product, .reveal, .from-left, .from-right, .pop, .draw, .finale .spark, .bar span { animation: none !important; }
  .stat .num { animation: none; --num: var(--target); }
}
</style>
"""


# =====================================================================
# 3. SMALL HELPER FUNCTIONS
# =====================================================================

def safe(text):
    """Stop Streamlit reading dollar signs as maths formulas."""
    return text.replace("$", "&#36;")


def wrap_marked(text, marker, css_class):
    """Wrap every piece of text between two markers in a styled span, e.g. **7** -> <span class="figure">7</span>."""
    parts = text.split(marker)
    result = ""
    for i in range(len(parts)):
        if i % 2 == 1:
            result = result + '<span class="' + css_class + '">' + parts[i] + '</span>'
        else:
            result = result + parts[i]
    return result


def highlight(text):
    """**key figures** become bold coloured numbers; ==key phrases== get a highlighter-pen underline."""
    return wrap_marked(wrap_marked(safe(text), "==", "mark"), "**", "figure")


def image_src(filename):
    """Read an image from the images folder and return it as text the page can show, or "" if it is missing."""
    path = os.path.join(IMAGE_FOLDER, filename)
    if not os.path.exists(path):
        return ""
    image_type = "png"
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        image_type = "jpeg"
    if filename.lower().endswith(".svg"):
        image_type = "svg+xml"
    file = open(path, "rb")
    encoded = base64.b64encode(file.read()).decode()
    file.close()
    return "data:image/" + image_type + ";base64," + encoded


def logo_html(filename, initials, shape):
    """Show a logo edge to edge ("fill", for the coloured company logos) or inside a white "box" (schools).
    If the file is missing, show the initials instead."""
    src = image_src(filename)
    if src == "":
        return '<div class="logo ' + shape + ' badge">' + initials + '</div>'
    return '<img class="logo ' + shape + '" alt="' + initials + ' logo" src="' + src + '">'


def html(text):
    """Show a block of HTML/CSS (never JavaScript) on the page."""
    st.markdown(text, unsafe_allow_html=True)


def page_header(title, icon, subtitle, next_key):
    """Page title and subtitle on the left, a Next button on the right (so it is visible without scrolling)."""
    left, right = st.columns([3, 1.5], vertical_alignment="bottom")
    if title != "":
        left.markdown('<h2 class="ptitle"><span class="ico">' + icon + '</span>' + title + '</h2>'
                      + '<p class="sub">' + subtitle + '</p>', unsafe_allow_html=True)
    if next_key != "":
        right.button("Next: " + page_label(next_key) + "  →", key="next_" + next_key, width="stretch",
                     on_click=go_to, args=(next_key,))


def part_title(title, icon):
    html('<h3 class="part"><span class="ico">' + icon + '</span>' + title + '</h3>')


def page_label(key):
    """The label of a page, e.g. "skills" -> "Skills & Education"."""
    for page in PAGES:
        if page[0] == key:
            return page[2]
    return ""


def go_to(key):
    """Button action: switch to another page."""
    st.session_state["page"] = key


def use_sample_job():
    """Button action: put the sample job description into the paste box."""
    st.session_state["jd"] = SAMPLE_JOB


def clear_job():
    st.session_state["jd"] = ""


def clean_words(text):
    """Lower-case a job description and turn punctuation into spaces, so keywords can be matched as whole words."""
    text = text.lower().replace("/", "").replace("-", " ")
    for mark in [",", ".", ";", ":", "(", ")", "!", "?", "\n", "&", "'", '"']:
        text = text.replace(mark, " ")
    return " " + " ".join(text.split()) + " "


def mentions(padded_text, keywords):
    """Return True if any keyword appears as a whole word or phrase in the text."""
    for word in keywords:
        if " " + word + " " in padded_text:
            return True
    return False


def build_text_resume():
    """Build a plain-text copy of the resume from the same data, for the download button."""
    lines = [PROFILE["short_name"].upper(), PROFILE["tagline"],
             "LinkedIn: " + PROFILE["linkedin"], "Email: " + PROFILE["email"], ""]
    for paragraph in PROFILE["intro"]:
        lines.append(paragraph.replace("**", "").replace("==", ""))
    lines.append("")
    lines.append("SKILLS")
    for group in SKILL_GROUPS:
        names = []
        for skill in group["skills"]:
            names.append(skill[1])
        lines.append("- " + group["title"] + ": " + ", ".join(names))
    lines.append("")
    lines.append("EXPERIENCE")
    for job in EXPERIENCE:
        lines.append(job["role"] + ", " + job["company"] + " (" + job["place"] + ", " + job["dates"] + ")")
        for point in job["points"]:
            lines.append("  - " + point.replace("**", ""))
    lines.append("")
    lines.append("PROJECTS")
    for project in PROJECTS:
        lines.append(project["title"] + " (" + project["meta"] + ", " + project["dates"] + ")")
        for point in project["points"]:
            lines.append("  - " + point.replace("**", ""))
    lines.append("")
    lines.append("EDUCATION")
    for school in EDUCATION:
        lines.append(school["degree"] + ", " + school["school"] + " (" + school["years"] + ")")
        lines.append("  Coursework: " + school["coursework"])
    lines.append("")
    lines.append("LEADERSHIP & ACTIVITIES")
    for item in LEADERSHIP:
        lines.append(item["title"] + " (" + item["role"] + ")")
        for point in item["points"]:
            lines.append("  - " + point.replace("**", ""))
    return "\n".join(lines)


# =====================================================================
# 4. PAGES  (one function per page in the sidebar directory)
# =====================================================================

def draw_sidebar():
    """Left-hand panel: element tile, status, the page directory and the text resume download."""
    sb = st.sidebar
    tile = ('<div class="tile"><div class="row"><span>' + PROFILE["tile_top_left"] + '</span><span>'
            + PROFILE["tile_top_right"] + '</span></div><div class="sym">' + PROFILE["symbol"]
            + '</div><div class="nm">' + PROFILE["short_name"] + '</div><div class="cap">'
            + PROFILE["tile_caption"] + '</div></div>')
    sb.markdown(tile, unsafe_allow_html=True)
    sb.markdown('<p class="side-name">' + PROFILE["name"] + '</p><p class="side-tag">' + PROFILE["tagline"] + '</p>'
                + '<div class="status"><i></i>' + PROFILE["status"] + '</div>'
                + '<p class="dir-title">Directory</p>', unsafe_allow_html=True)
    for page in PAGES:
        label = "**" + page[1] + "** \u2003" + page[2]
        if st.session_state["page"] == page[0]:
            sb.button(label, key="nav_" + page[0], type="primary", width="stretch", on_click=go_to, args=(page[0],))
        else:
            sb.button(label, key="nav_" + page[0], width="stretch", on_click=go_to, args=(page[0],))
    sb.download_button("Download text resume", data=build_text_resume(),
                       file_name="Kenny_Wang_Resume.txt", mime="text/plain")
    sb.markdown('<p class="updated">Last updated: ' + PROFILE["last_updated"] + '</p>', unsafe_allow_html=True)


def page_about():
    page_header("", "", "", "skills")
    page = '<div class="hero-grid reveal"><div class="photo-col">'
    photo = image_src(PROFILE["photo"])
    if photo != "":
        page = page + '<img class="portrait" alt="Portrait of ' + PROFILE["short_name"] + '" src="' + photo + '">'
    page = (page + '</div><div><div class="hero-name">' + PROFILE["name"] + '</div><div class="hero-tag">'
            + PROFILE["tagline"] + '</div><div class="intro">')
    for paragraph in PROFILE["intro"]:
        page = page + '<p>' + highlight(paragraph) + '</p>'
    page = page + '</div><div class="facts">'
    for fact in PROFILE["facts"]:
        page = page + '<div><span class="e">' + fact[2] + '</span><span class="k">' + fact[0] + '</span><span>' + highlight(fact[1]) + '</span></div>'
    page = page + '</div></div></div><div class="stats reveal">'
    for item in HIGHLIGHTS:
        page = (page + '<div class="stat"><div class="num" style="--target:' + str(item["value"])
                + '; --suffix:\'' + item["suffix"] + '\'"></div><div class="lbl">' + safe(item["label"]) + '</div></div>')
    page = page + '</div>'
    html(page)


def page_skills_education():
    page_header("Skills & Education", ICONS["skills"], "My periodic table of tools, and where I learned them.", "work")
    part_title("My Periodic Table", ICONS["skills"])
    page = '<div class="ptable reveal">'
    for group in SKILL_GROUPS:
        page = page + '<div class="prow" style="--g: var(--' + group["colour"] + ')"><div class="gl">' + group["title"] + '</div>'
        for skill in group["skills"]:
            page = (page + '<div class="el"><span class="s">' + skill[0] + '</span><span class="n">' + skill[1]
                    + '</span><span class="d">' + skill[2] + '</span></div>')
        page = page + '</div>'
    page = page + '</div>'
    html(page)

    part_title("Education", ICONS["education"])
    page = '<div class="edus reveal">'
    for school in EDUCATION:
        page = (page + '<div class="edu"><div class="edu-head">' + logo_html(school["logo"], school["initials"], "box")
                + '<div><p class="yr">' + school["years"] + ' (' + school["note"] + ')</p><h4>' + school["degree"] + '</h4></div></div>'
                + '<p class="detail">' + school["school"] + '</p>'
                + '<p class="detail">Coursework: ' + school["coursework"] + '</p></div>')
    page = page + '</div>'
    html(page)


def page_experience_projects():
    page_header("Experience & Projects", ICONS["experience"],
                "Two internships, one in strategic advisory and one in ESG consulting, and my analytics projects.", "leadership")
    part_title("Professional Experience", ICONS["experience"])
    page = '<div class="jobs reveal">'
    for job in EXPERIENCE:
        page = (page + '<div class="job"><div class="job-head">' + logo_html(job["logo"], job["initials"], "fill")
                + '<div><h4>' + job["role"] + '</h4><p class="org">' + job["company"] + ', ' + job["place"]
                + ', ' + job["dates"] + '</p></div></div><ul>')
        for point in job["points"]:
            page = page + '<li>' + highlight(point) + '</li>'
        page = page + '</ul></div>'
    page = page + '</div>'
    html(page)

    part_title("Projects", ICONS["projects"])
    page = '<div class="cards reveal">'
    for project in PROJECTS:
        page = (page + '<div class="card" style="--g: var(--' + project["colour"] + ')"><p class="when">'
                + project["dates"] + '</p><h4>' + project["title"] + '</h4><p class="meta">' + project["meta"] + '</p><ul>')
        for point in project["points"]:
            page = page + '<li>' + highlight(point) + '</li>'
        page = page + '</ul><div class="chips">'
        for tool in project["tools"]:
            page = page + '<span class="chip">' + tool + '</span>'
        page = page + '</div></div>'
    page = page + '</div>'
    html(page)


def page_leadership_beyond():
    page_header("Leadership & Beyond", ICONS["leadership"], "Where I lead, team up and give back.", "job-match")
    part_title("Leadership & Activities", ICONS["leadership"])
    page = '<div class="ccards three reveal">'
    for item in LEADERSHIP:
        page = (page + '<div class="ccard" style="--g: var(--' + item["colour"] + ')"><div class="top"><span class="emoji">'
                + item["emoji"] + '</span><div><h4>' + item["title"] + '</h4><span class="pill">' + item["role"]
                + '</span></div></div><ul>')
        for point in item["points"]:
            page = page + '<li>' + highlight(point) + '</li>'
        page = page + '</ul></div>'
    page = page + '</div>'
    html(page)

    part_title("Beyond Work", ICONS["beyond"])
    page = '<div class="ccards two reveal">'
    for interest in INTERESTS:
        page = (page + '<div class="ccard" style="--g: var(--' + interest[3] + ')"><div class="top"><span class="emoji">'
                + interest[2] + '</span><div><h4>' + interest[0] + '</h4><span class="pill">' + interest[4]
                + '</span></div></div><p>' + safe(interest[1]) + '</p></div>')
    page = page + '</div>'
    html(page)


def page_job_match():
    page_header("Job Match", ICONS["job-match"], "Recruiters: paste a job description and see where my experience fits. "
                "It is a simple keyword check, so treat it as a conversation starter.", "contact")
    if "jd" not in st.session_state:
        st.session_state["jd"] = ""
    b1, b2, gap = st.columns([1.9, 0.7, 2.4])
    b1.button("Try a sample job description", on_click=use_sample_job, width="stretch")
    b2.button("Clear", on_click=clear_job, width="stretch")
    box = st.container(key="jdbox")
    job_text = box.text_area("📋 Paste a job description here", key="jd", height=120,
                             placeholder="Paste the job advert text, then press Ctrl+Enter (or click outside the box).")
    if job_text.strip() == "":
        st.info("Paste a job description above, or try the sample, to see the match.")
        return

    words = clean_words(job_text)
    matched = []
    for rule in MATCH_RULES:
        if mentions(words, rule["keywords"]):
            matched.append(rule)
    learning = []
    for rule in LEARNING_RULES:
        if mentions(words, rule["keywords"]):
            learning.append(rule)

    total = len(matched) + len(learning)
    if total == 0:
        st.info("I could not spot any skills I recognise yet. Try pasting a longer job description.")
        return
    score = round(len(matched) / total * 100)

    left, right = st.columns([1, 2.4])
    left.markdown('<p class="score">' + str(score) + '%</p><p>' + str(len(matched)) + ' of ' + str(total)
                  + ' skills in this job description are ones I have already used.</p><div class="bar"><span style="width:'
                  + str(score) + '%"></span></div>', unsafe_allow_html=True)
    evidence = '<p class="ev-title">Evidence I bring</p><div class="evs">'
    for rule in matched:
        evidence = evidence + '<div class="ev"><b>' + rule["skill"] + '</b><span>' + safe(rule["evidence"]) + '</span></div>'
    evidence = evidence + '</div>'
    if len(learning) > 0:
        evidence = evidence + '<p class="ev-title">What I still need to learn</p><div class="gaps">'
        for rule in learning:
            evidence = evidence + '<span>' + rule["skill"] + '</span>'
        evidence = evidence + '</div>'
    right.markdown(evidence, unsafe_allow_html=True)


def contact_form_html():
    """The email form as plain HTML (no JavaScript), the same as on the static page.
    method="get" turns the chosen subject and the message into a normal email in the visitor's email app."""
    options = ""
    for purpose in CONTACT_PURPOSES:
        options = options + '<option value="' + purpose[1] + '">' + purpose[0] + '</option>'
    # &#10; is a new line inside the message box (a blank line would end the HTML block)
    starter = "Hi Kenny,&#10;&#10;&#10;&#10;Best regards,&#10;"
    return ('<form class="mailform" action="mailto:' + PROFILE["email"] + '" method="get">'
            '<label>What is this about?<select name="subject">' + options + '</select></label>'
            '<label>Your message<textarea name="body" rows="7" required>' + starter + '</textarea></label>'
            '<p class="tip">Tip: mention your name, your organisation and the role or project. '
            'Your email address is included automatically when you send.</p>'
            '<button type="submit">✉️&nbsp; Send email</button></form>')


def page_contact():
    page_header("Contact me", ICONS["contact"], "Hiring for a role, or have a project in mind? The reaction below is what I hope we can build together.", "")

    # The reaction: Kw + Your team -> Insight, assembling when the page opens
    sparks = ""
    offsets = [["-40vw", "-30px", "-90deg"], ["-28vw", "60px", "45deg"], ["-16vw", "-70px", "-30deg"],
               ["-6vw", "80px", "120deg"], ["6vw", "-80px", "-120deg"], ["16vw", "70px", "30deg"],
               ["28vw", "-60px", "-45deg"], ["40vw", "30px", "90deg"]]
    count = 0
    for group in SKILL_GROUPS:
        for skill in group["skills"]:
            if group["colour"] != "lithium" and count < len(offsets):
                o = offsets[count]
                sparks = (sparks + '<span class="spark" style="--x:' + o[0] + '; --y:' + o[1] + '; --r:' + o[2]
                          + '; animation-delay:' + str(round(0.3 + count * 0.1, 1)) + 's">' + skill[0] + '</span>')
                count = count + 1
    reaction = st.container(key="reaction")
    reaction.markdown('<div class="finale"><div class="eq">'
                      '<div class="rx from-left" style="--c: var(--copper)"><span class="rs">' + PROFILE["symbol"]
                      + '</span><span class="rn">Kenny</span></div><span class="op pop">+</span>'
                      '<div class="rx from-right" style="--c: var(--sodium)"><span class="rs">Yt</span><span class="rn">Your team</span></div>'
                      '<span class="arrow draw"></span>'
                      '<div class="rx product" style="--c: var(--lithium)"><span class="rs">In</span><span class="rn">Insight</span></div>'
                      '</div><div class="sparks">' + sparks + '</div>'
                      '<p>Catalyst: an analyst internship, part-time from Jan 2027 and full-time from Mar 2027.</p></div>',
                      unsafe_allow_html=True)
    middle = reaction.columns([2, 1, 2])[1]
    if middle.button("Start the reaction", type="primary", width="stretch"):
        st.balloons()

    left, right = st.columns([1.5, 1], gap="medium")
    left.markdown(contact_form_html(), unsafe_allow_html=True)
    right.markdown('<div class="linkedin"><h3>Prefer LinkedIn?</h3>'
                   '<p>Connect with me or send me a message there. Either way, I would be glad to hear from you.</p>'
                   '<p><b style="color:#FFFFFF">Open to:</b> analyst internships, part-time Jan–Feb 2027 and full-time '
                   'Mar–Dec 2027, and analytics project collaborations.</p>'
                   '<a class="li-btn" href="' + PROFILE["linkedin"] + '" target="_blank"><span class="li-badge">in</span>'
                   'Connect on LinkedIn</a></div>', unsafe_allow_html=True)


# =====================================================================
# 5. RUN THE APP
# =====================================================================

st.set_page_config(page_title=PROFILE["short_name"] + " | Resume", page_icon="🧪",
                   layout="wide", initial_sidebar_state="auto")
html(CSS)
if "page" not in st.session_state:
    st.session_state["page"] = "about"

draw_sidebar()
current = st.session_state["page"]
if current == "about":
    page_about()
elif current == "skills":
    page_skills_education()
elif current == "work":
    page_experience_projects()
elif current == "leadership":
    page_leadership_beyond()
elif current == "job-match":
    page_job_match()
else:
    page_contact()
