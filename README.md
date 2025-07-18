# 🎮 GameHub – A Flask-Based Mini Projects Platform

---

## ⚠️ Project Status

> 🛠️ This is a **private, personal project** currently under **irregular development**.  
> Although not updated on a fixed schedule, this project reflects my experimental ideas,  
> and I actively shape it further during creative bursts and breaks.  
> It's not production-ready yet — but it’s growing into something meaningful over time.

> 📌 Expect future improvements, better UI, and added features — whenever inspiration strikes!

---

## 🚀 Features

- 🧩 Combines 8+ fun & functional mini-projects into one hub
- 🔥 Powered by **Flask backend** with **Jinja2 templating**
- 🗃️ Integrated **database support** (e.g., scores, chat history)
- 🖼️ Shared layout using `base.html` for clean UI and consistency
- 🎯 Modular structure (inspired by Django-style routing)
- 🧪 Ideal for personal learning, demos, and experimentation

---

## 🌐 Live Demo

🔗 **[Coming Soon...]** *(Or insert your deployed link if hosted)*

---

## 📁 Project Structure

```bash
gamehub/
├── static/               # CSS, JS, images
├── templates/            # HTML templates (Jinja2)
│   ├── base.html         # Shared layout
│   ├── index.html        # Home Dashboard
│   ├── chatbot.html      # Chatbot interface
│   ├── encoder.html      # Encoder/decoder tool
│   ├── hangman.html      # Hangman game
│   ├── quiz.html         # Quiz app
│   ├── stock.html        # Stock viewer tool
│   ├── swg.html          # Rock-Paper-Scissors game
│   ├── time_greet.html   # Time-based greeter
├── app.py                # Main Flask app
├── models.py             # SQLAlchemy models (if used)
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
```

---
## 🧩 Included Mini-Projects

| Feature         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **Chatbot**     | Simple NLTK-style chatbot that replies using predefined rules               |
| **Encoder**     | Encode or decode text using Caesar cipher or binary logic                   |
| **Hangman**     | Classic hangman game with random word selection                             |
| **Quiz**        | Quiz app with scoring system and question sets                              |
| **Stock Viewer**| Mock/static stock value fetcher (can be extended with live API)             |
| **SWG**         | "Stone-Win-Gun" — a fun Rock-Paper-Scissors variant                         |
| **Time Greeter**| Shows a greeting (Good Morning/Afternoon/Evening) based on system time      |
| **Dashboard**   | Central hub (`index.html`) to access all mini-projects                      |

---

## 🛠️ Tech Stack
Backend: Flask (Python)

Templating: Jinja2

Frontend: HTML5, CSS3, JavaScript

Database: SQLite (via SQLAlchemy, optional)

Extra: NLTK (for chatbot), Bootstrap (optional for styling)

---

## 🔧 Setup Instructions
Clone this repo:
```
git clone https://github.com/yourusername/gamehub.git
cd gamehub
```

Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install requirements:

```
pip install -r requirements.txt
```

Run the app:

```
flask run
```

Visit:
```
http://localhost:5000/
```

---

## 📌 Future Plans
🔐 Add user login/signup

🏆 Save scores and display leaderboards

📱 Make fully responsive for mobile

🎨 Improve layout with better UI/UX

---

## 📜 License
This is a private learning project. Forking or copying for learning is encouraged — credits appreciated.
