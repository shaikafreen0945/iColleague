🧑‍💼 iColleague – Virtual Employee Assistant
📌 Problem Statement

In many organizations, employees repeatedly contact HR or managers to ask for internal contact details and process-related information such as leave policy, IT support, and onboarding steps.
This leads to repeated interruptions, delayed responses, and reduced productivity.

✅ Solution

iColleague – Virtual Employee Assistant is a simple web-based application built using Streamlit that allows employees to instantly access:

Internal contact details

Organizational process and policy information

The assistant provides quick responses through an easy-to-use interface, reducing dependency on HR and improving employee experience.

🛠️ Technology Stack

Frontend & UI: Streamlit (Python)

Backend Logic: Python

Database: In-memory data / Can be extended to MySQL or SQLite

IDE: VS Code

⚙️ Features

Chat-style input for employee queries

Search internal contacts (HR, IT Support, Admin, etc.)

View common process information (Leave policy, onboarding steps)

Fast and user-friendly interface

Easy to extend with database or API integration

📂 Project Structure
iColleague/
│
├── app.py                  # Main Streamlit application
├── venv/                   # Python virtual environment
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation

▶️ How to Run the Project
1️⃣ Clone or Download the Project

Place the project folder on your system.

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment

Windows (CMD):

venv\Scripts\activate.bat


Windows (PowerShell):

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\activate

4️⃣ Install Dependencies
pip install streamlit


(Optional)

pip freeze > requirements.txt

5️⃣ Run the Application
streamlit run app.py


The application will open in your browser at:

http://localhost:8501

🧪 Sample Queries

“Who is the HR manager?”

“What is the leave approval process?”

“IT support contact details”

🎯 Benefits

Reduces repetitive employee queries

Saves HR and admin time

Improves information accessibility

Scalable for future enhancements

🚀 Future Enhancements

Database integration (MySQL / SQLite)

Natural language processing

Authentication for employees

Deployment on cloud (AWS / Azure)
