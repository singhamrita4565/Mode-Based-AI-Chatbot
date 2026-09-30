# 🤖 Mode Based AI Chatbot

## 📌 Description

Mode Based AI Chatbot is an interactive conversational AI application developed using **Python, Streamlit, LangChain, and Mistral AI**.

The application allows users to interact with an AI chatbot while choosing from different personality modes. Each mode changes the way the AI responds to the user's messages.
The chatbot currently provides three different personalities:

* 😡 **Angry AI** – Responds in an aggressive and impatient style.
* 😂 **Funny AI** – Responds with humor, jokes, and a light-hearted style.
* 😢 **Sad AI** – Responds in an emotional and sad style.

The application maintains the conversation history during the session, allowing the AI to understand previous messages and provide more contextual responses. Users can also reset the conversation and start a fresh chat whenever required.

The Mistral AI API is connected through **LangChain**, while the API key is securely stored in a `.env` file using `python-dotenv`.

## ✨ Features

* 🤖 AI-powered conversations
* 🎭 Multiple AI personality modes
* 💬 Conversation history
* 🔄 Reset chat functionality
* 🔐 Secure API key management using `.env`
* 🖥️ Interactive Streamlit interface
* ⚡ Real-time AI responses

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **LangChain**
* **Mistral AI**
* **python-dotenv**

## 📂 Project Structure

```text
Mode-Based-AI-Chatbot/
│
├── app.py
├── .env
├── README.md
└── requirements.txt
```

## 📦 Installation

Install the required packages:

```bash
pip install streamlit langchain langchain-mistralai python-dotenv
```

## 🔑 Environment Setup

Create a `.env` file in the project folder:

```env
MISTRAL_API_KEY=your_api_key_here
```

Keep your API key private and do not upload the `.env` file to GitHub.

## ▶️ Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## 💡 How It Works

1. The application loads the Mistral API key from the `.env` file.
2. The user selects an AI personality.
3. A system message defines the selected personality.
4. The user enters a message through the Streamlit chat interface.
5. LangChain sends the conversation history to the Mistral AI model.
6. The model generates a response according to the selected personality.
7. The response is displayed in the chatbot interface.
8. The conversation is stored in Streamlit's session state.

## 🔄 Reset Chat

The **Reset Chat** button clears the existing conversation and starts a new conversation using the currently selected personality.

## 🚀 Future Improvements

* Add more AI personalities.
* Add voice input and voice responses.
* Add chat export functionality.
* Add a dark/light theme.
* Add user authentication.
* Store conversations permanently in a database.
* Add model selection options.
