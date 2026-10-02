import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="AI Job Salary Prediction",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Job Salary Prediction")
st.write("Enter the job details below to predict the salary.")

# ---------------------------------------------------------
# LOAD TRAINED MODEL
# ---------------------------------------------------------
model = joblib.load("salary_prediction_model (1).pkl")

# ---------------------------------------------------------
# SKILL COLUMNS
# These are the EXACT columns used in your dataset/model
# ---------------------------------------------------------
skill_columns = [
    'skill_AWS',
    'skill_Azure',
    'skill_Computer Vision',
    'skill_Data Visualization',
    'skill_Deep Learning',
    'skill_Docker',
    'skill_GCP',
    'skill_Git',
    'skill_Hadoop',
    'skill_Java',
    'skill_Kubernetes',
    'skill_Linux',
    'skill_MLOps',
    'skill_Mathematics',
    'skill_NLP',
    'skill_PyTorch',
    'skill_Python',
    'skill_R',
    'skill_SQL',
    'skill_Scala',
    'skill_Spark',
    'skill_Statistics',
    'skill_Tableau',
    'skill_TensorFlow'
]

# ---------------------------------------------------------
# SIDEBAR - JOB INFORMATION
# ---------------------------------------------------------
st.sidebar.header("Job Information")

job_title = st.sidebar.text_input(
    "Job Title",
    value="AI Research Scientist"
)

employment_type = st.sidebar.selectbox(
    "Employment Type",
    ["FT", "PT", "CT", "FL"]
)

company_location = st.sidebar.text_input(
    "Company Location",
    value="United States"
)

company_name = st.sidebar.text_input(
    "Company Name",
    value="Tech Company"
)

employee_residence = st.sidebar.text_input(
    "Employee Residence",
    value="United States"
)

industry = st.sidebar.text_input(
    "Industry",
    value="Technology"
)

experience_level = st.sidebar.selectbox(
    "Experience Level",
    ["EN", "MI", "SE", "EX"]
)

company_size = st.sidebar.selectbox(
    "Company Size",
    ["S", "M", "L"]
)

education_required = st.sidebar.selectbox(
    "Education Required",
    [
        "Bachelor",
        "Master",
        "PhD",
        "Associate"
    ]
)

# ---------------------------------------------------------
# NUMERICAL FEATURES
# ---------------------------------------------------------
st.sidebar.header("Job Details")

years_experience = st.sidebar.number_input(
    "Years of Experience",
    min_value=0,
    max_value=50,
    value=2,
    step=1
)

remote_ratio = st.sidebar.slider(
    "Remote Ratio",
    min_value=0,
    max_value=100,
    value=50,
    step=10
)

job_description_length = st.sidebar.number_input(
    "Job Description Length",
    min_value=0,
    value=1000,
    step=100
)

benefits_score = st.sidebar.number_input(
    "Benefits Score",
    min_value=0.0,
    max_value=10.0,
    value=5.0,
    step=0.1
)

# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
st.sidebar.header("Skills")

skill_values = {}

for skill in skill_columns:

    # Remove "skill_" only for displaying checkbox name
    display_name = skill.replace("skill_", "")

    skill_values[skill] = int(
        st.sidebar.checkbox(display_name)
    )

# ---------------------------------------------------------
# CREATE INPUT DATA
# ---------------------------------------------------------
input_data = {
    "job_title": job_title,
    "employment_type": employment_type,
    "company_location": company_location,
    "company_name": company_name,
    "employee_residence": employee_residence,
    "industry": industry,
    "experience_level": experience_level,
    "company_size": company_size,
    "education_required": education_required,

    "years_experience": years_experience,
    "job_description_length": job_description_length,
    "benefits_score": benefits_score,
    "remote_ratio": remote_ratio
}

# Add the 24 skill columns
input_data.update(skill_values)

# Convert to DataFrame
input_df = pd.DataFrame([input_data])

# ---------------------------------------------------------
# SHOW INPUT DATA
# ---------------------------------------------------------
st.subheader("Input Information")

col1, col2 = st.columns(2)

with col1:
    st.write("### Job Details")

    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Experience Level:** {experience_level}")
    st.write(f"**Employment Type:** {employment_type}")
    st.write(f"**Company:** {company_name}")
    st.write(f"**Industry:** {industry}")

with col2:
    st.write("### Experience & Work")

    st.write(f"**Years of Experience:** {years_experience}")
    st.write(f"**Remote Ratio:** {remote_ratio}%")
    st.write(f"**Education:** {education_required}")
    st.write(f"**Company Size:** {company_size}")

# ---------------------------------------------------------
# SELECTED SKILLS
# ---------------------------------------------------------
selected_skills = [
    skill.replace("skill_", "")
    for skill, value in skill_values.items()
    if value == 1
]

st.write("### Selected Skills")

if selected_skills:
    st.write(", ".join(selected_skills))
else:
    st.write("No skills selected.")

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
st.divider()

if st.button(
    "💰 Predict Salary",
    use_container_width=True
):

    try:

        prediction = model.predict(input_df)[0]

        st.success(
            f"### 💰 Predicted Salary: ${prediction:,.2f}"
        )

    except Exception as e:

        st.error(
            "Prediction failed. Please check that the input "
            "columns match the columns used when training the model."
        )

        st.exception(e)

# ---------------------------------------------------------
# OPTIONAL: SHOW MODEL INPUT
# ---------------------------------------------------------
with st.expander("View Model Input"):

    st.dataframe(
        input_df,
        use_container_width=True
    )