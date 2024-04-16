import streamlit as st
from openai import OpenAI

st.title('GenAI App - AI Code Reviewer')
st.header('Code Reviewer')

f = open('my_key.txt')
OPENAI_API_KEY = f.read()
client = OpenAI(api_key = OPENAI_API_KEY)

query = st.text_area('Enter Query : ')
if st.button('HIT ME'):
    with st.spinner('Please Wait............'):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "code corrections and buggs recognization"},
                {"role": "user", "content": query}
            ]
        )
        st.write(response.choices[0].message.content)
