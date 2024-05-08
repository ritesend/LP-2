import streamlit as st
from typing import List

knowledge_base = {
    "software_developer" : [
        "1: Web Developer",
        "2: Android Developer",
        "3: Data Analyst",
        "4: Java Developer"
    ],

    "digital_markerting_specialist": [
        "1: Social Media Manager"
        "2: SEO Specialist",
        "2: Content Marketer",
        "4: Please learn digital marketing tools like Google Analytics , Canva."
    ],

    "financial_analyst": [
        "1: Investment Analyst",
        "2: Risk Manager",
        "3: Financial Planner",
        "4: Please develop strong analytical and quantative skills."
    ],

    "business_owner" : [
        "1: Entrepreneur",
        "2: Small Business Owner",
        "3: Startup Founder",
        "4: Please focus on building leadership,management,and business development skills"
    ],

    "healthcare_professional" : [
        "1: Physician",
        "2: Surgeon",
        "3: Nurse",
        "4: Physical Therapist",
        "5: Psychiatrist"
    ]
}

st.header("Career Guide Expert System")

def respond(input: List[str]):
    skills,interests,traits,careerGoals = input
    
    if (skills == "programming" and "problem solving" in interests and "analytical" in traits and "software industry" in careerGoals):
        st.write("Based on your inputs,recommended pursuing a career as software developer!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["software_developer"]:
            st.write(i)
        
    elif (skills == "marketing" and "creative" in interests and "social" in traits and "digital industry" in careerGoals):
        st.write("Based on your inputs,recommended pursuing a career as a digital marketing specicalist!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["digital_markerting_specialist"]:
            st.write(i)
    
    elif (skills == "financial analysis" and "analytical" in interests and "detailed-oriented" in traits and "finance industry" in careerGoals):
        st.write("Based on your inputs,recommended pursuing a career as a financial analyst!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["financial_analyst"]:
            st.write(i)

    elif (skills == "leadership" and "innovative" in interests and "management" in traits and "entrepreneurship" in careerGoals):
        st.write("Based on your inputs,recommended pursuing a career as a business owner!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["business_owner"]:
            st.write(i)

    elif (skills == "medical" and "responsible" in interests and "empathetic" in traits and "healthcare industry" in careerGoals):
        st.write("Based on your inputs,recommended pursuing a career in Medical Field!")
        st.write("Here are some career paths and recommendations:")
        for i in knowledge_base["healthcare_professional"]:
            st.write(i)

    else:
        st.write("We couldn't find a suitable career recommendation based on your inputs.")
if __name__ == "__main__":
    skills = st.selectbox("Select your skills:",["programming","marketing","financial analysis","leadership","medical"])
    interests = st.multiselect("Select your interests:",["problem solving","creative","analytical","innovative","responsible"])
    traits = st.multiselect("Select your personality traits:",["analytical","social","detailed-oriented","management","empathetic"])
    careerGoals = st.multiselect("Select your career goals:",["software industry","digital industry","finance industry","entrepreneurship","healthcare industry"])

    if st.button("Get Career Recommendations"):
        respond([skills,interests,traits,careerGoals])
    if (quit):
        st.write("Thank you for using the Expert system!")
