import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt","cute dinosaur")
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail apprerance of the input. Response it shortly in around 20 words.",
    }]
    gpt_prompt.append({
        "role": "user",
        "content": user_input,
    })
    with st.spinner("Waiting for ChatGPT..."):
      gpt_response = openai.ChatCompletion.create(
          model = "gpt-3.5-turbo",
          messages = gpt_prompt,
      )    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for DALL-E..."):
      dalle_response = openai.Image.create(
        prompt = prompt,
        size = "512x512",
      )
    st.image(dalle_response["data"][0]["url"])

