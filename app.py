import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Function to get AI response
def get_ai_response(user_input):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant knowledgeable about startup funding."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Streamlit UI
def main():
    st.title("Startup Incubator AI Assistant")
    st.write("Ask me anything about startup funding!")

    user_input = st.text_input("Enter your question here:")

    if st.button("Submit"):
        if user_input:
            with st.spinner("Thinking..."):
                ai_response = get_ai_response(user_input)
                st.write("### Response:")
                st.write(ai_response)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()