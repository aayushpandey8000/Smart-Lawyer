import streamlit as st
import openai
import os

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.title("Smart Lawyer")

# Define image size
image_width = 210

# Load and display image
image = "law.jpg"  # Change this to the path of your image
col1, col2 = st.columns([4, 8])
with col1:
    st.image(image, width=image_width)

# User input for the incident description
with col2:
    incident_description = st.text_area("Please describe the incident:")

# Button to trigger response
if st.button("Get Legal Advice"):
    # Formulate prompt based on incident description
    prompt = f"Based on the incident described in India: {incident_description} What relevant legal section(s) should be imposed, and what would be the appropriate penalty or years of imprisonment, if applicable? Please explain the chosen section(s) briefly."

    # Call the language model to generate legal advice
    response = openai.Completion.create(
        engine="davinci-002",
        prompt=prompt,
        temperature=0.6,  # Adjust temperature for increased randomness
        max_tokens=250
    )

    # Display the response
    st.write("Legal Advice:")
    st.write(response.choices[0].text.strip())
