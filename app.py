
import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Job Salary Prediction",
    page_icon="💰",
    layout="wide"
)


# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load("salary_prediction_model.pkl")


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("💰 AI Job Salary Prediction")
st.write(
    "Enter the job details below to predict the expected salary."
)

st.divider()


# --------------------------------------------------
# Input Fields
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    job_title = st.text_input(
        "Job Title",
        placeholder="Example: Data Scientist"
    )

    experience_level = st.selectbox(
        "Experience Level",
        ["EN", "MI", "SE", "EX"]
    )

    employment_type = st.selectbox(
        "Employment Type",
        ["Full-time", "Part-time", "Contract", "Freelance"]
    )

    company_location = st.text_input(
        "Company Location",
        placeholder="Example: United States"
    )

    company_size = st.selectbox(
        "Company Size",
        ["Small", "Medium", "Large"]
    )

    company_name = st.text_input(
        "Company Name",
        placeholder="Example: ABC Company"
    )

    employee_residence = st.text_input(
        "Employee Residence",
        placeholder="Example: United States"
    )


with col2:

    education_required = st.selectbox(
        "Education Required",
        ["Associate", "Bachelor", "Master", "PhD"]
    )

    years_experience = st.number_input(
        "Years of Experience",
        min_value=0,
        max_value=50,
        value=2
    )

    required_skills = st.text_input(
        "Required Skills",
        placeholder="Python, SQL, Machine Learning"
    )

    job_description_length = st.number_input(
        "Job Description Length",
        min_value=0,
        value=1000
    )

    industry = st.text_input(
        "Industry",
        placeholder="Example: Technology"
    )

    remote_ratio = st.selectbox(
        "Remote Ratio",
        [0, 50, 100]
    )

    benefits_score = st.number_input(
        "Benefits Score",
        min_value=0.0,
        max_value=10.0,
        value=5.0
    )

    salary_currency = st.selectbox(
        "Salary Currency",
        ["USD", "EUR", "GBP", "CAD", "AUD"]
    )


# --------------------------------------------------
# Prediction Button
# --------------------------------------------------

st.divider()

if st.button("🔮 Predict Salary", type="primary"):

    # Create input dataframe
    input_data = pd.DataFrame({
        "job_title": [job_title],
        "experience_level": [experience_level],
        "employment_type": [employment_type],
        "company_location": [company_location],
        "company_size": [company_size],
        "company_name": [company_name],
        "employee_residence": [employee_residence],
        "education_required": [education_required],
        "years_experience": [years_experience],
        "required_skills": [required_skills],
        "job_description_length": [job_description_length],
        "industry": [industry],
        "remote_ratio": [remote_ratio],
        "benefits_score": [benefits_score],
        "salary_currency": [salary_currency]
    })


    # Predict salary
    prediction = model.predict(input_data)[0]


    # Display result
    st.success("Salary Prediction Completed!")

    st.metric(
        label="Predicted Salary",
        value=f"${prediction:,.2f}"
    )

    st.info(
        "The predicted salary is an estimated value based on the "
        "information provided."
    )

