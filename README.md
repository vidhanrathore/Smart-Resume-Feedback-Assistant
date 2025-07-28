🧠 Smart Resume Analyzer
An AI-powered resume feedback tool that uses Groq-hosted LLMs (like LLaMA 3) to instantly analyze, score, and suggest improvements to your resume. Built with Python + Streamlit for an easy-to-use interface and lightning-fast inference.

🌟 Features
📄 Upload PDF or DOCX resumes

⚡ Instant resume parsing and feedback

🧠 Suggestions on skills, formatting, and content

📊 AI-generated score out of 100

🔥 Powered by Groq’s ultra-low-latency LLMs

🖼️ High-Level Architecture
Here's a high-level flow of how the app works:

vbnet
Copy
Edit
              ┌──────────────────────────────┐
              │        User Interface         │
              │       (Streamlit App)         │
              └────────────┬─────────────────┘
                           │
                           ▼
              ┌──────────────────────────────┐
              │   Resume Upload + Extract    │
              │ - PyMuPDF / python-docx       │
              └────────────┬─────────────────┘
                           │
                           ▼
              ┌──────────────────────────────┐
              │      Prompt Construction     │
              │ - Custom prompt to Groq LLM  │
              └────────────┬─────────────────┘
                           │
                           ▼
              ┌──────────────────────────────┐
              │     Groq API (LLM Model)     │
              │ - LLaMA 3 or Mixtral         │
              └────────────┬─────────────────┘
                           │
                           ▼
              ┌──────────────────────────────┐
              │  Output: Feedback, Score,    │
              │  Suggestions                 │
              └──────────────────────────────┘
📂 Project Structure
vbnet
Copy
Edit
resume-analyzer/
├── app.py                  ← Streamlit UI logic  
├── resume_parser.py        ← Resume parsing (PDF/DOCX)  
├── prompts.py              ← Prompt template for LLM  
├── groq_api.py             ← Groq API integration  
├── requirements.txt        ← Python dependencies  
└── README.md               ← Project documentation
🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
2. Create Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Set Up Groq API Key
Set your Groq API Key as an environment variable:

On Windows:

bash
Copy
Edit
set GROQ_API_KEY=your_key_here
On Mac/Linux:

bash
Copy
Edit
export GROQ_API_KEY=your_key_here
5. Run the App
bash
Copy
Edit
streamlit run app.py
🚀 Usage
Launch the app

Upload your resume (.pdf or .docx)

Wait for Groq's LLM to analyze it

View strengths, weaknesses, suggestions, and score

🔍 Example Prompt
The app sends the following prompt to the LLM:

vbnet
Copy
Edit
You are a resume reviewer. Analyze the following resume and give feedback:
1. Strengths  
2. Weaknesses  
3. Skills to add  
4. Formatting suggestions  
5. Score out of 100

Resume Text:
[resume content here]
📦 Dependencies
streamlit

PyMuPDF (fitz)

python-docx

requests

Install using:

bash
Copy
Edit
pip install -r requirements.txt
📌 To Do / Future Improvements
Match resume to job description

Export AI feedback as PDF

Track feedback history

Improve UI with animations or themes

🧠 Powered by
Groq LPU Inference Engine

LLaMA 3 or Mixtral

Python & Streamlit

🤝 Contributing
Pull requests and feedback are welcome!
If you want to contribute, fork the repo and submit a PR.

📄 License
This project is licensed under the MIT License.