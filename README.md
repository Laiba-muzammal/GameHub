# 🎮 GameHub – A Flask-Based Mini Projects Platform

**GameHub** is a full-stack Flask application combining multiple fun and useful mini-projects into one web platform. It uses **Flask**, **HTML/CSS/JS**, and an integrated **database** for user data and score storage (where applicable).

---

## 🚀 Features

- 🔥 Built with **Flask** and modular **Jinja2 templates**
- 🧠 Includes 8+ mini apps and utilities
- 💾 Database support for scores, messages, or quiz results
- 🎨 Clean UI with `base.html` for layout reuse
- 🧩 Organized route structure (like Django-style modularity)

---

## 🌐 Live Demo

🔗 **[Coming Soon...]** *(Add deployed link or localhost instructions)*

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
│   ├── stock.html        # Mock stock checker
│   ├── swg.html          # Stone-paper-scissors game
│   ├── time_greet.html   # Time-based greeting feature
├── app.py                # Main Flask app
├── models.py             # DB models (if using SQLAlchemy)
├── routes/               # (Optional) Modular route files
├── requirements.txt      # Python dependencies
└── README.md             # Project overview
```

---

## 🧩 Included Mini-Projects
App/Feature	Description
Chatbot	Simple NLTK-style chatbot with predefined rules
Encoder	Encode/decode messages (Caesar shift or binary)
Hangman	Classic hangman game with random word logic
Quiz	Quiz app with scoring logic and question sets
Stock Viewer	Static or mock API-based stock value fetcher
SWG	Stone-Win-Gun (Rock-Paper-Scissors variant)
Time Greeter	Shows dynamic greeting based on system time
Dashboard (Index)	Central hub to access all features

---

## 🛠️ Tech Stack
Backend: Flask (Python)

Templating: Jinja2

Frontend: HTML5, CSS3, JavaScript

Database: SQLite (or your preferred DB via SQLAlchemy)

Optional Tools: NLTK (for chatbot), Bootstrap (for styling)

---

## 🔧 Setup Instructions
#### Clone this repo:

```
git clone https://github.com/yourusername/gamehub.git
cd gamehub
```

#### Create and activate a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### Install dependencies:
```
pip install -r requirements.txt
```

#### Run the app:

```
flask run
```

### Visit:
```
http://localhost:5000/
```

---

### 📌 Future Plans
Add user login/logout functionality

Store quiz scores or game results in DB

Add leaderboard feature

Make it mobile responsive

---

### 📜 License
This project is open-source. Feel free to fork, use, and contribute.

---

### 🙌 Acknowledgements
Thanks to open-source libraries and inspiration from daily coding fun! 🎉
