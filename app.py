# -*- coding: utf-8 -*-

! pip install streamlit
#!pip install streamlit google-generativeai textblob dotenv

pip install load_dotenv

!pip install -U -q google.generativeai # Install the Python SDK

import streamlit as st
from google.cloud import aiplatform
from google.oauth2 import service_account
from google.protobuf import json_format
import load_dotenv
import google.generativeai as genai
from google.colab import userdata

def generate_response(resume_text, job_description, prompt, extra_words):
    # Set up Gemini API client with your API key
    endpoint ='llmats.com'
    api_key=userdata.get('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')


    response = model.generate_content(prompt+' '+extra_words+ ' '+resume_text+' '+job_description)
    return response.text

st.title("AI-Powered Resume Builder and Revamp")

resume_text = st.text_area("Paste your resume here:")
job_description = st.text_area("Paste the job description here:")

prompt = st.text_area("Enter your prompt (instructions for the AI):",
                      value="Rewrite my resume to align with this job description.")
extra_words = st.number_input("Additional words (optional):", value=200)

if st.button("Generate Improved Resume"):
    response_text = generate_response(resume_text, job_description, prompt, extra_words)
    st.text_area("Improved Resume:", response_text)

def edit_resume(resume_text):
    # ... Similar structure to generate_response, but using a fixed
    #     prompt for resume editing
    endpoint ='llmats.com'
    api_key=userdata.get('GOOGLE_API_KEY')
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    prompt = ''' using the above recommendations rephrase all of my resume bullets ,
    like an expert in professional career advisor with expertise in resume making of 10 years and an experiences hiring manager.
    Do not add any false/new information. '''
    response = model.generate_content(prompt+' '+resume_text)

st.subheader("Further Refinement (Optional)")
if st.button("Edit Resume Bullets"):
    modified_resume = edit_resume(response_text)
    st.text_area("Modified Resume:", modified_resume)

