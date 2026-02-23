import streamlit as st
import numpy as np
import joblib
import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

placement_model = joblib.load("placement_model.pkl")
study_model = joblib.load("study_recommendation_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="Placement Predictor", layout="centered")

dark_mode = st.toggle("🌙 Dark Mode")

if dark_mode:
    bg_color = "#0E1117"
    card_color = "#1c1f26"
    text_color = "white"
    header_gradient = "linear-gradient(135deg, #000000, #434343)"
else:
    bg_color = "#e6e9ef"
    card_color = "white"
    text_color = "black"
    header_gradient = "linear-gradient(135deg, #243b55, #141e30)"
st.markdown(f"""
<style>

/* App background */
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

/* Force normal text color */
p, h1, h2, h3, h4, h5, h6, label, span {{
    color: {text_color} !important;
}}

/* Main Card */
.main-card {{
    background: {card_color};
    padding: 40px;
    border-radius: 15px;
    max-width: 750px;
    margin: auto;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}}

/* Header */
.header-section {{
    background: {header_gradient};
    height: 140px;
    border-radius: 15px 15px 0 0;
    clip-path: polygon(0 0, 100% 0, 100% 75%, 0 100%);
    display: flex;
    align-items: center;
    padding-left: 30px;
}}

.header-title {{
    color: white;
    font-size: 26px;
    font-weight: bold;
}}

/* Selectbox text fix */
div[data-baseweb="select"] > div {{
    color: black !important;
    background-color: white !important;
}}

/* Dropdown options */
ul[role="listbox"] li {{
    color: black !important;
    background-color: white !important;
}}

/* Text input */
input {{
    color: black !important;
}}

/* Buttons */
.stButton > button {{
    background-color: #243b55 !important;
    color: white !important;
    border-radius: 8px;
    padding: 10px 25px;
    font-weight: 600;
}}

.stButton > button:hover {{
    background-color: #1b2d44 !important;
    color: white !important;
}}

</style>
""", unsafe_allow_html=True)

if "page" not in st.session_state:
st.session_state.page = 1
if st.session_state.page == 1:
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="header-section"><div class="header-title">PLACEMENT READINESS SYSTEM</div></div>', unsafe_allow_html=True)
st.write("## 🎓 AI Powered Placement & Study Recommendation")
st.write("A smart analytics system designed to evaluate placement readiness and recommend optimized study hours.")
st.write("---")
if st.button("START ASSESSMENT"):
    st.session_state.page = 2
st.markdown('</div>', unsafe_allow_html=True)
elif st.session_state.page == 2:
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="header-section"><div class="header-title">ENTER STUDENT DETAILS</div></div>', unsafe_allow_html=True)

st.write("## 👤 Student Information")

name = st.text_input("Full Name")

email = st.text_input("Email Address")

college = st.text_input("College Name")

st.write("---")

st.write("## 🎓 Academic Details")

year = st.selectbox("Year of Study", [3, 4])

cgpa = st.slider("CGPA", 0.0, 10.0, 0.0)

internships = st.slider("Internships", 0, 5, 0)

projects = st.slider("Projects", 0, 10, 0)

st.write("---")

st.write("## 📘 Preparation Details")

aptitude = st.slider("Aptitude Hours", 0, 12, 0)

coding = st.slider("Coding Hours", 0, 12, 0)

mock = st.slider("Mock Interviews Given", 0, 10, 0)

attention = st.slider("Total Study Hours", 0, 12, 0)

if st.button("GENERATE REPORT"):

    features = np.array([[year, cgpa, internships, projects,

                          aptitude, coding, mock, attention]])

    features_scaled = scaler.transform(features)

    probability = placement_model.predict_proba(features_scaled)[0][1]

    recommended_hours = study_model.predict(features)[0]

    recommended_hours = np.clip(recommended_hours, 2, 10)

    st.session_state.readiness = round(probability * 100, 2)

    st.session_state.study_hours = round(recommended_hours, 2)

    st.session_state.name = name

    st.session_state.email = email

    st.session_state.college = college

    st.session_state.page = 3

st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == 3:

readiness = st.session_state.readiness

hours = st.session_state.study_hours

st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="header-section"><div class="header-title">PLACEMENT ANALYSIS RESULT</div></div>', unsafe_allow_html=True)

st.write("## 📊 Prediction Summary")

st.metric("Placement Probability", f"{readiness}%")

st.metric("Recommended Study Hours", f"{hours} hrs/day")

if readiness >= 75:

    suggestions = [

        "Participate in coding contests",

        "Participate in Aptitude Tests",

        "Continue giving more mock interviews",

        "Maintain consistency"

    ]

elif readiness >= 50:

    suggestions = [

        "Solve 1 hard DSA problem daily",

        "Revise DBMS & OS",

        "Practice aptitude with timer",

        "Increase consistency"

    ]

else:

    suggestions = [

        "Strengthen DSA basics",

        "Solve 3 easy problems daily",

        "Revise core subjects",

        "Increase study time seriously"

    ]

st.write("---")

st.write("## 📌 Improvement Plan")

for s in suggestions:

    st.write("•", s)

def generate_pdf():

    file_path = "Placement_Report.pdf"

    doc = SimpleDocTemplate(file_path, pagesize=A4)

    elements = []

    styles = getSampleStyleSheet()



    elements.append(Paragraph("Placement Readiness Report", styles["Heading1"]))

    elements.append(Spacer(1, 0.3 * inch))



    today = datetime.date.today().strftime("%d-%m-%Y")

    elements.append(Paragraph(f"Date: {today}", styles["Normal"]))

    elements.append(Spacer(1, 0.3 * inch))



    student_data = [

        ["Name", st.session_state.name],

        ["Email", st.session_state.email],

        ["College", st.session_state.college]

    ]



    student_table = Table(student_data, colWidths=[2*inch, 3*inch])

    student_table.setStyle(TableStyle([

        ('GRID', (0,0), (-1,-1), 1, colors.grey),

        ('BACKGROUND', (0,0), (0,-1), colors.lightgrey),

    ]))



    elements.append(student_table)

    elements.append(Spacer(1, 0.5 * inch))



    result_data = [

        ["Placement Probability", f"{readiness}%"],

        ["Recommended Study Hours", f"{hours} hrs/day"]

    ]



    result_table = Table(result_data, colWidths=[3*inch, 2*inch])

    result_table.setStyle(TableStyle([

        ('GRID', (0,0), (-1,-1), 1, colors.grey),

        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),

    ]))



    elements.append(result_table)

    elements.append(Spacer(1, 0.5 * inch))



    elements.append(Paragraph("Suggested Improvement Plan:", styles["Heading2"]))

    elements.append(Spacer(1, 0.2 * inch))



    bullet_points = [ListItem(Paragraph(item, styles["Normal"])) for item in suggestions]

    elements.append(ListFlowable(bullet_points, bulletType='bullet'))



    doc.build(elements)

    return file_path



pdf_file = generate_pdf()



with open(pdf_file, "rb") as file:

    st.download_button(

        label="📥 Download PDF Report",

        data=file,

        file_name="Placement_Report.pdf",

        mime="application/pdf"

    )



if st.button("START AGAIN"):

    st.session_state.page = 1



st.markdown('</div>', unsafe_allow_html=True)
