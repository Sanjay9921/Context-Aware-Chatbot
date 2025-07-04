# Context Aware LLM Chatbot

# 1. Project Overview
An interactive chatbot that allows users to upload PDFs and ask natural language questions based on their contents. The chatbot uses a language model API and intelligent preprocessing to provide context-aware answers.

Deployable on Streamlit Cloud, this tool is perfect for students, researchers, and professionals who want a lightweight document Q&A system.

## Streamlit App Link to test
Please use this [link](https://kunjibettu-context-aware-chatbot.streamlit.app/) to test my app :)

# 2. Features
* Upload and process smaller-medium sized (<20 pages) PDF file
* Chunk and preprocess text using `Langchain`
* Ask questions in `English` and get smart, context-based answers
* Powered by `Together API` (limited usage quota)
* Deployed on `Streamlit` web app.

# 3. Tech Stack
* Streamlit – For the interactive web app interface
* Together AI API – For LLM inference (Mistral 7B Instruct)
* Langchain – For text chunking and retrieval

# 4. Installation
```bash
git clone https://github.com/Sanjay9921/Context-Aware-LLM-Chatbot.git
cd Context-Aware-LLM-Chatbot

# if you wish to deploy on your local system
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

# 5. Configuration

## 5.1 API Keys and LLM Model selection
* Make sure that you have registered on [Together AI](https://api.together.ai/)
* You will get an API key
* You can use the model `meta-llama/Llama-3.3-70B-Instruct-Turbo-Free`

## 5.2 Deployment

> [!TIP]
> Deploying the app on Streamlit cloud is faster and cleaner than local as you do not have to install anything on your local system

### 5.2.1 Local
* Create a `.env` file in the root directory
* Add the following API:
```bash
TOGETHER_API_KEY=your_api_key_here
```
* Run the streamlit app using the following command:
```bash
streamlit run app.py
```
* The application will open in: `http://localhost:8501/`

### 5.2.2 Streamlit Cloud
* Create a new Github repository
* Push the code to the new repository and go to [StreamLit](https://share.streamlit.io/)
* Select the option to deploy via your Github app
* Add your secret API key in the `Secrets` section before deploying in the following `TOML` format:
`TOGETHER_API_KEY="your_api_key_here"`

# Citations

* Chase, H. (2022). LangChain [Computer software]. https://github.com/langchain-ai/langchain