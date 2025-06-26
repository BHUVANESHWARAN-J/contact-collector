# 📇 Smart Contact Collector

A professional, lightweight Streamlit web application that allows users to dynamically create forms, collect responses, and store them directly into Google Sheets. Ideal for custom surveys, contact collection, and feedback systems with real-time data updates.

---

## 🚀 Features

- ✅ Dynamic form creation with editable questions
- 📤 Response storage directly in Google Sheets using the Google Sheets API
- 🔄 Live data editing and management capabilities
- 📊 Clean tabular display of submitted entries
- 🔐 Secure handling of credentials using `service_account.json` (excluded from Git)

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
git clone https://github.com/BHUVANESHWARAN-J/smart-contact-collector.git
cd smart-contact-collector

shell


### 2. Install Python Dependencies

pip install -r requirements.txt

Or manually:

pip install streamlit gspread oauth2client


### 3. Google Sheets Setup

- Create a Google Service Account from https://console.cloud.google.com/
- Enable the Google Sheets API
- Download the `service_account.json` credentials file
- Share your target Google Sheet with the service account email (xxx@project.iam.gserviceaccount.com)

Place `service_account.json` in the project root, but ensure it is listed in `.gitignore` to avoid exposing sensitive data.

---

## ▶️ Run the App

streamlit run app.py



---

## 📁 Project Structure

smart-contact-collector/
├── app.py # Main Streamlit app
├── generate.py # Dynamic form and sheet logic
├── utils.py # Helper functions
├── config.py # Configuration settings
├── service_account.json # Google API credentials (private)
├── .gitignore # Ignore sensitive files
└── README.md # Project documentation



---

## 🔐 .gitignore (Security Notice)

Ensure the following line exists in `.gitignore`:

service_account.json

This prevents accidental exposure of credentials on GitHub.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to submit a pull request or open an issue for any improvements, suggestions, or bugs.

---

## 🧑‍💻 Author

**Bhuvaneshwaran J**  
📬 bhuvane419@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/bhuvaneshwaran-j-b80a35255/
