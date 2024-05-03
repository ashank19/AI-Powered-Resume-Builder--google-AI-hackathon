import streamlit as st
import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(resume_text, prompt,info,temperature,user_input):
    # Set up Gemini API client with your API key
    #endpoint ='llmats.com'
    #api_key=userdata.get('GOOGLE_API_KEY')
    #genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro',generation_config=genai.GenerationConfig(
        max_output_tokens=200000,
        temperature=temperature,
    ))


    response = model.generate_content(prompt+' '+user_input+' '+resume_text+' '+info)
    return response.text

st.title("AI-Powered Personalized Invite/connect")

resume_text = st.text_area("Paste your resume here:")
relevant_info = st.text_area("Paste the job description / other information from some linkedin post/info here:")

prompt = """Act like a skilled and experienced career advisor use the information provided in my resume along with the relevant instructions to write a personalized message/invite to a recruiter.
                      
You must consider the job market is very competitive and make sure the message is not more than 200 words including the initial Greetings and spaces in the message."""
user_input = st.text_area("Additional instructions")

temperature = st.slider("Selection  for Accuracy/Generalizable Output", min_value=0.0, max_value=1.0, step=0.01)

if temperature<=0.33:
    st.write('More resume specific Output')
elif temperature>0.33 and temperature<=0.66:
    st.write('Balanced results neither accurate nor generalizable')
elif temperature>0.66:
    st.write('Highly General output may not be relevant to the resume')


if st.button("Generate Personalized Invite"):
    response_text = generate_response(resume_text, prompt, temperature,relevant_info,user_input)
    st.text_area("Personalized Invite:", response_text)

