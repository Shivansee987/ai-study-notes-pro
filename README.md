

 📝 Project Title:

**AI-Based Study Notes Chatbot

---

 1. Abstract

This project is an AI-powered chatbot that helps students interact with their study materials through a user-friendly interface. It supports real-time question-answering using AI models, note management, and intelligent categorization of queries.

---

 2. Problem Statement

Students often struggle to manage and search through large volumes of academic content. Finding specific answers quickly becomes difficult without structure or guidance.

---

 3.Objective

To build a simple yet powerful web application that:

* Uses AI to answer academic questions.
* Provides a clean UI to chat with the bot.
* Categorizes student queries intelligently.

---

 4. Tech Stack Used

| Layer          | Technology                          |
| -------------- | ----------------------------------- |
| Frontend       | React.js (Vite)                     |
| Backend        | Python (FastAPI)                    |
| Language Model | OpenAI (or dummy for local testing) |
| Deployment     | Localhost / Azure-ready             |

---
 5. System Architecture

```plaintext
User --> React Frontend --> FastAPI Backend --> AI Model
                          --> Categorization Logic
```

*(Add a diagram if you want)*

---

 6. Key Features

 🔹 Chatbot for Q\&A

Handles user questions and returns instant AI-generated answers.

🔹 Intelligent Categorization of Notes *(Newly Integrated)*

Automatically detects the topic of user queries like Math, Programming, etc.

 🔹 Simple and Clean UI

Built with React, allowing easy interaction and message history display.

---

 7.How to Run the Project

 🛠 Backend (FastAPI)

```bash
cd backend
uvicorn app:app --reload
```

🛠 Frontend (React)

```bash
cd frontend
npm install
npm run dev
```

---

 8. Screenshots(Add these manually)

* Chat UI
* Categorized response sample
* Terminal output (if needed)

---

 9.Conclusion

This chatbot simplifies academic learning with a focus on clarity and organization. The new categorization feature enhances usability and makes information retrieval faster.

---

 10.Future Scope

* Store categorized notes in a database
* NLP-based category prediction
* Multi-language support
* Resume & document parsing features (enhancement)


