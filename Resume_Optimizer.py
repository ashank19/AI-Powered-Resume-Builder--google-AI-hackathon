# -*- coding: utf-8 -*-
import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def generate_response(resume_text, job_description, prompt,temperature):
    # Set up Gemini API client with your API key
    #endpoint ='llmats.com'
    #api_key=userdata.get('GOOGLE_API_KEY')
    #genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro',generation_config=genai.GenerationConfig(
        max_output_tokens=200000,
        temperature=temperature,
    ))


    response = model.generate_content(prompt+' '+resume_text+' '+job_description)
    return response.text

st.title("AI-Powered Resume Builder and Revamp")

resume_text = st.text_area("Paste your resume here:")
job_description = st.text_area("Paste the job description here:")

prompt = st.text_area("Prompt to evaluate Resume you can make changes as per your requirement",
                      value="""Act like a skilled or experienced application tracking system(ATS) and an experienced hiring manager 
With a deep understanding of Tech field( Data Analyst/Scientist, Machine Learning, Big Data, product sense, product analytics)
You must consider the job market is very competitive and you must provide the assistance for improving the resume and make my profile standout and leave no stone unturned to shortlist my resume for this position. 
leave no stone unturned 
Also assign the percentage match based on the Job Description(JD) and the missing keywords with high accuracy.
resume : {text} 
description:{JD}
I want response in a single line in the form of string having structure 
{{"JD Match" : "%", 
"Missing Keywords :[]"")""")
#extra_words = st.text_area("Additional words (optional limit 200):")

temperature = st.slider("Selection  for Accuracy/Generalizable Output", min_value=0.0, max_value=1.0, step=0.01)

if temperature<=0.33:
    st.write('More JD Specific Output')
elif temperature>0.33 and temperature<=0.66:
    st.write('Balanced results neither accurate nor generalizable')
elif temperature>0.66:
    st.write('Highly General output may not be relevant to the Job description')



if st.button("Generate Improved Resume"):
    response_text = generate_response(resume_text, job_description, prompt, temperature)
    st.text_area("Improved Resume:", response_text)

def edit_resume(resume_text):
    # ... Similar structure to generate_response, but using a fixed
    #     prompt for resume editing
    #endpoint ='llmats.com'
    #api_key=userdata.get('GOOGLE_API_KEY')
    #genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = ''' using the above recommendations rephrase all of my resume bullets ,
    like an expert in professional career advisor with expertise in resume making of 10 years and an experiences hiring manager.
    Do not add any false/new information. '''
    response = model.generate_content(prompt+' '+resume_text)

    return response.text

st.subheader("Further Refinement (Optional)")
if st.button("Edit Resume Bullets"):
    modified_resume = edit_resume(resume_text)
    st.text_area("Modified Resume:", modified_resume)

