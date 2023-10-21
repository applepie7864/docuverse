# docuverse
A streamlit document chatbot application using LLM from HuggingFace API

![Application](./img-folder/docuverse-img.png)

### Setup:
I'm using 64-bit Python v3.6.9
1. Clone this repository
   - git clone https://github.com/applepie7864/docuverse.git
2. Setup your python virtual environment
   - python -m venv your_environment_name
   - source your_environment_name/bin/activate
3. Install dependencies
   - pip3 install streamlit pypdf2 langchain python-dotenv faiss-cpu huggingface_hub InstructorEmbedding sentence_transformers watchdog
4. Create key file
   - Create a file named '.env'
   - Get your Huggingface inference key following this short tutorial: https://www.youtube.com/watch?v=jo_fTD2H4xA
   - Inside this file write: HUGGINGFACEHUB_API_TOKEN=your_token

### How it Works:
