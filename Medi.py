import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

# Initialize the OpenAI model with your API key
llm = OpenAI(api_key='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')


# Define a prompt template for querying
prompt_template = PromptTemplate(
    input_variables=["data_description", "question"],
    template="""
    You are a data analyst. Here is the data you have:
    {data_description}

    Based on this data, answer the question: {question}
    """
)

# Create a LangChain
chain = LLMChain(llm=llm, prompt=prompt_template)

def get_response(data_description, question):
    # Running the chain to get a response based on the data description and a question
    response = chain.run(data_description=data_description, question=question)
    return response

# Streamlit app
st.title("Welcome to MediCore 🤖🌟!")
st.write("Hey love, welcome to MediCore! I’m Medi, your digital mental health companion — here to support you with empathetic conversations.")

st.sidebar.title('Symptom Checker 🩺')
selected_symptom = st.sidebar.radio(
    "# How do you feel today?",
    ('😔 Feeling Anxious', '😞 Feeling Depressed', '😓 Feeling Stressed', '🛌 Trouble Sleeping', '🤕 Physical Symptoms')
)
st.sidebar.title('Daily Motivation 💬')
motivation_quote = st.sidebar.text('You are stronger than you think. Take it one step at a time.')

# Main content

question = st.text_input("How do you feel?")
if st.button("⟫"):
    if question:
        answer = get_response(data_description, question)
        st.write("### Answer")
        st.write(answer)
    else:
        st.write("Please enter a question.")
