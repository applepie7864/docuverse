import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms.huggingface_hub import HuggingFaceHub
from html_templates import css, bot_template, user_template

def handle_input(query):
    if not st.session_state.convo:
        st.write("Error: You must provide a document.")
    else:  
        response = st.session_state.convo({'question': query})
        st.session_state.chat_history = response['chat_history']
        
        for i, msg in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(user_template.replace("{{question}}", msg.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace("{{answer}}", msg.content), unsafe_allow_html=True)

# Extract raw text from a list of PDF's
def extract_pdf_text(documents):
    raw_text = ""
    for document in documents:
        pdf_reader = PdfReader(document)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
    return raw_text

# Create list of chunks of text from a given string
def create_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    text_chunks = text_splitter.split_text(raw_text)
    return text_chunks

# Make the embeddings and configure our vector database
def configure_db(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    knowledgebase = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return knowledgebase 

# Create a conversation chain so that chat history is retained
def get_conversation_chain(knowledgebase):
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever=knowledgebase.as_retriever(),
        memory=memory
    )
    return conversation_chain
    
def main():
    load_dotenv()
    st.set_page_config(page_title="Docuverse", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    
    if "convo" not in st.session_state:
        st.session_state.convo = None
        
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None  
    
    st.header("Docuverse :books:")
    query = st.text_input("Talk to your Documents!")
    
    if query:
        handle_input(query)

    with st.sidebar:
        st.subheader("Your Documents")
        documents = st.file_uploader("Upload your PDF's here:", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = extract_pdf_text(documents)
                text_chunks = create_text_chunks(raw_text)
                knowledgebase = configure_db(text_chunks)
                st.session_state.convo = get_conversation_chain(knowledgebase)
                

if __name__ == '__main__':
    main()